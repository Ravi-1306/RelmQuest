from flask import Flask, render_template, request, redirect, abort, session, flash
from flask_socketio import SocketIO, emit, rooms, join_room, leave_room
from flask_uploads import UploadSet, configure_uploads
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from src.models import db, Account
from src.db_actions import db_function
from PIL import Image
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv('APP_SECRET_KEY', 'secret')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.getenv("DB_USER")}:{os.getenv("DB_PASS")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/realmquest'

photos = UploadSet('photos', ('jpg', 'jpeg', 'jpe', 'jif'))
app.config['UPLOADED_PHOTOS_DEST'] = 'static/assets/chars/'
configure_uploads(app, photos)

db.init_app(app)
socketio = SocketIO(app)
bcrypt = Bcrypt(app)

##Needed for Websocket hotloading users on page.
users_on_location = {}

@socketio.on('message_sent')
def handle_message(message_text, city_name):
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    message_id = db_function.insert_city_message(message_text, character.id, 
                                    character.account_id,
                                    character.name, 
                                    character.image, city_name)
    message = db_function.get_city_message(city_name, message_id)
    emit('chat', (message.message, message.id, character.name, character.image, str(message.time_stamp)), to= city_name)

@socketio.on('connect')
def handle_connect():
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    print(f"{session['username']}: connected")

@socketio.on('connection')
def connection(city_name):
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not users_on_location.get(city_name):
        users_on_location[city_name] = [(character.name, character.image)]
    else:
        users_on_location[city_name] = users_on_location[city_name] + [(character.name, character.image)]
    join_room(f'{city_name}')
    emit('new_connection', (character.name, character.image), to= city_name)

@socketio.on('disconnect')
def handle_disconnect():
    if 'username' in session.keys():
        account = db_function.get_account_id_from_username(session['username'])
        character = db_function.get_character_data(account)
        for city_users in users_on_location.values():
            for user in city_users:
                if user == (character.name, character.image):
                    city_users.remove(user)
        for room in rooms():
            leave_room(room=room)
            emit('disconnection', character.name, to= room)

@app.get("/")
def get_home_page():
    username = session.get('username')
    show_username = False
    if username:
        if 'visited_home' in session:
            show_username = True
        else:
            session['visited_home'] = True
    return render_template('Home_page.html', username=username, show_username=show_username)
    # return render_template('Home_page.html')

@app.get("/Worldmap")
def get_world_map():
    return render_template('Worldmap_page.html')

@app.get("/Worldmap/<country_name>")
def get_country(country_name):
    country= db_function.get_country(country_name)
    if not country:
        flash("Country not found", "404")
        return redirect('/Worldmap')
    location_list= db_function.get_location_by_country(country.id)
    return render_template('Countries.html', country_name= country_name, list= location_list)

@app.get("/Location/<city_name>")
def get_city(city_name: str):
    city = db_function.get_city(city_name)
    if not city:
        flash("Location not Found.", "404")
        return redirect('/')
    events = db_function.get_all_events_for_city(city.id)
    messages = db_function.get_city_messages_50(city.name)
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not character:
        flash('Character Not Found. Please create one.', '404')
        return redirect('/')
    user_list = users_on_location.get(city_name)
    if not user_list:
        users = []
    else:
        users = [user for user in user_list]
    return render_template('Cities.html', city_name = city.name
                           , character = character, events = events,
                           messages = messages, users = users)

@app.post("/Location/<city_name>")
def edit_message_city(city_name: str):
    city = db_function.get_city(city_name)
    if not city:
        flash("Location not Found.", "404")
        return redirect('/')
    message_id = request.form.get('message_id')
    message_change = request.form.get('message_edit')
    if not message_id or not message_id.isdigit():
        flash('Bad data. Message not provided or is not a number.', '400')
        return redirect(f'/Location/{city_name}')
    if not message_change:
        flash('Please provide a message.', '400')
        return redirect(f'/Location/{city_name}')
    message = db_function.get_city_message(city_name, int(message_id))
    if not message:
        flash('Message Not Found', '404')
        return redirect(f'/Location/{city_name}')
    if 'username' not in session:
        flash('User not in Session. Please Log in.', 'Not_Authenticated 401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    if account != message.account_id:
        flash('Not Authorized to Edit', '403')
        return redirect('/')
    db_function.edit_city_message(message.id, city_name, message_change)
    socketio.emit('message_updated', (message.id, message.message ), to= city_name)
    return redirect(f'/Location/{city_name}')

@app.post("/Location/<city_name>/delete")
def delete_message_city(city_name: str):
    message_id = request.form.get('message_id')
    if not message_id or not message_id.isdigit():
        flash('Bad data. Message not provided or is not a number.', '400')
        return redirect(f'/Location/{city_name}')
    message = db_function.get_city_message(city_name, int(message_id))
    if not message:
        flash('Message Not Found', '404')
        return redirect(f'/Location/{city_name}')
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    if account != message.account_id:
        flash('Not Authorized to Edit', '403')
        return redirect('/')
    socketio.emit('message_delete', message.id, to= city_name)
    db_function.remove_city_message(city_name, message)
    return redirect(f'/Location/{city_name}')

@app.get("/Rules")
def get_rule():
    return render_template('Rules.html')

@app.get("/CharacterCreation")
def get_character_creation():
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/Login')
    classes = db_function.get_classes()
    races = db_function.get_races()
    return render_template('Character_Creation.html', classes = classes, races = races)

@app.post("/CharacterCreation")
def create_character():
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/Login')
    if [x for x in (db_function.get_account_id_from_username(session['username']),
                        request.form.get('Character-Name'),
                        request.form.get('Age'),
                        request.form.get('Race'), 
                        request.form.get('Alignment'),
                        request.form.get('Personality'), 
                        request.form.get('Religion'), 
                        request.form.get('classSelect'), 
                        request.form.get('equipmentSet'), 
                        request.form.get('stats1'),
                        request.form.get('stats2'), 
                        request.form.get('stats3'), 
                        request.form.get('stats4'), 
                        request.form.get('stats5'), 
                        request.form.get('Backstorytxtbx'), 
                        request.form.get('Descriptiontxtbx'),
                        request.form.get('startingLocation')) 
                        if x is None]:
        flash("please fill all fields", "404")
        return redirect("/CharacterCreation")

    user_id = db_function.get_account_id_from_username(session['username'])    
    character_Name = request.form.get('Character-Name')
    try:
        character_Age = int(request.form.get('Age'))
        if int(character_Age) < 1:
            flash("please enter valid value for age", "404")
            return redirect("/CharacterCreation")
    except:
            flash("please enter valid value for age", "404")
            return redirect("/CharacterCreation")
    try:
        character_Race =int(request.form.get('Race')) 
        character_Race = db_function.get_race(character_Race)
        if not character_Race:
            flash("please enter valid value", "400")
            return redirect("/CharacterCreation")
    except:
            flash("please enter valid value for Race", "404")
            return redirect("/CharacterCreation")  
    try:        
        character_Alignment =int(request.form.get('Alignment'))
        if character_Alignment < 1 or character_Alignment > 9:
            flash("please enter valid value for Alignment", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for Alignment", "400")
        return redirect("/CharacterCreation")
    
    character_Personality = request.form.get('Personality')
    character_Religion = request.form.get('Religion')

    try:        
        character_Class = int(request.form.get('classSelect'))
        character_Class = db_function.get_class(character_Class)
        if not character_Class:
            flash("please enter valid value for Character Class", "400")
            return redirect("/CharacterCreation")
    except:
            flash("please enter valid value for Character Class", "400")
            return redirect("/CharacterCreation")
    try:
        character_Grit =int(request.form.get('stats1'))
        if character_Grit < 1 or character_Grit > 20:
            flash("please enter valid value for Grit", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for Grit", "400")
        return redirect("/CharacterCreation")
    try:
        character_Prowess = int(request.form.get('stats2'))
        if character_Prowess < 1 or character_Prowess > 20:
            flash("please enter valid value for Prowess", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for Prowess", "400")
        return redirect("/CharacterCreation")
    try:     
        character_Grace = int(request.form.get('stats3'))
        if character_Grace < 1 or character_Grace > 20:
            flash("please enter valid value for Grace", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for Grace", "400")
        return redirect("/CharacterCreation")
    
    try:
        character_Wit = int(request.form.get('stats4'))
        if character_Wit < 1 or character_Wit > 20:
            flash("please enter valid value for wit", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for wit", "400")
        return redirect("/CharacterCreation") 
    try:        
        character_Savvy = int(request.form.get('stats5')) 
        if character_Savvy < 1 or character_Savvy > 20:
            flash("please enter valid value for savvy", "400")
            return redirect("/CharacterCreation")
    except:
        flash("please enter valid value for savvy", "400")
        return redirect("/CharacterCreation") 
    try:
        equipment = int(request.form.get('equipmentSet'))
        if equipment < 1 or equipment > 5:
            flash('Equipment set not valid.', '400')
            return redirect('/CharacterCreation')
    except:
        flash('Equipment set not valid.', '400')
        return redirect('/CharacterCreation')

    character_Backstory = request.form.get('Backstorytxtbx')
    character_Descriptiontxtbx = request.form.get('Descriptiontxtbx')
    ##figure out how to download the file then convert the name to a string 
    try:
        character_StartingLocation = int(request.form.get('startingLocation'))
        character_StartingLocation = db_function.get_location(character_StartingLocation)
        if not character_StartingLocation:
            flash('Starting Location not found.', '404')
            return redirect('/CharacterCreation')
    except:
        if not character_StartingLocation:
            flash('Starting Location not valid.', '400')
            return redirect('/CharacterCreation')
    if 'PlayerArt' in request.files.keys():  
        photo = request.files['PlayerArt']
        if photo.filename == '':
            flash('Problem with Image upload', '400')
            return redirect('/CharacterCreation')
        if not photos.file_allowed(photo, photo.filename):
            flash('Invalid image format', '400')
            return redirect('/CharacterCreation')
        with Image.open(photo) as img:
            img.thumbnail((50,50))
            filename = f'{character_Name}.jpg'
            img.save(f'static/assets/chars/{filename}', format='JPEG')
    else:
        filename = None
    character = db_function.make_Character(user_id,character_Name, character_Age, character_Race.id, character_Alignment, 
                                                character_Personality, character_Religion, character_Class.id,
                                                character_Grit, character_Prowess, character_Grace, character_Wit, character_Savvy,
                                                character_Backstory, character_Descriptiontxtbx, character_StartingLocation, filename)
    db_function.add_equipment_set(equipment, character)
    db_function.add_first_ability(character_Class.id, character)
    ##redirect needs fixing
    return redirect('/Character')

@app.get("/Lore")
def Lore_page():
    return render_template('Lore.html')

@app.get("/LevelUp")
def level_up():
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not character:
        flash('Character Not Found. Please create one.', '404')
        return redirect('/')
    char_class = db_function.get_char_class(character)
    level = db_function.calc_level(character.experience)
    abilities = db_function.get_abilities_for_level(level, character.race, character.char_class)
    if not abilities:
        abilities = []
    return render_template('level.html', character = character, abilities = abilities, level = level, char_class = char_class)

@app.post("/LevelUp")
def leveling():
    grit_inc = request.form.get("grit")
    if not grit_inc or not grit_inc.isdigit():
        flash('Grit not Valid', '400')
        return redirect('/LevelUp')
    prowess_inc = request.form.get("prowess")
    if not prowess_inc or not prowess_inc.isdigit():
        flash('Prowess not Valid', '400')
        return redirect('/LevelUp')
    grace_inc = request.form.get("grace")
    if not grace_inc or not grace_inc.isdigit():
        flash('Grace not Valid', '400')
        return redirect('LevelUp')
    wit_inc = request.form.get("wit")
    if not wit_inc or not wit_inc.isdigit():
        flash('Wit not Valid', '400')
        return redirect('LevelUp')
    savvy_inc = request.form.get("savvy")
    if not savvy_inc or not savvy_inc.isdigit():
        flash('Savvy not Valid', '400')
        return redirect('LevelUp')
    ability_choice = request.form.get("ability")
    if not ability_choice or not ability_choice.isdigit():
        flash('Ability choice not Valid', '400')
        return redirect('LevelUp')
    grit_inc = int(grit_inc)
    prowess_inc = int(prowess_inc)
    grace_inc = int(grace_inc)
    wit_inc = int(wit_inc)
    savvy_inc = int(savvy_inc)
    ability_choice = int(ability_choice)
    if 'username' not in session:
        flash('User not in Session. Please Log in.', '401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not character:
        flash('Character Not Found. Please create one.', '404')
        return redirect('/')
    if ability_choice != 0:
        ability = db_function.get_ability(int(ability_choice))
        if not ability:
            flash('Ability not Found', '404')
            return redirect('/LevelUp')
        if db_function.calc_level(character.experience)[0] <= ability.level:
            ability_choice = ability.id
    if grit_inc + prowess_inc + grace_inc + wit_inc + savvy_inc > 2 or grit_inc + prowess_inc + grace_inc + wit_inc + savvy_inc < 0:
        flash('Too many Ability Increases', '400')
        return redirect('/LevelUp')
    db_function.level_character(character, ability_choice, grit_inc, prowess_inc, grace_inc, wit_inc, savvy_inc)
    return redirect("/Character")

@app.route("/CreateAccount", methods = ["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form.get('User-Name')
        raw_password = request.form.get('User-Password')
        email = request.form.get('User-Email')
        if username == '' or raw_password == '' or email == '':
            # abort(401)
            flash('All fields are required.', 'error')
            return render_template("AccountCreation.html")
        existing_user = Account.query.filter_by(username=username).first()
        if existing_user:
            # abort(400)
            flash('Username already exists. Please try again with different username', 'error')
            return render_template("AccountCreation.html")
        existing_user = Account.query.filter_by(email = email).first()
        if existing_user:
            flash('Email is already used, please use a different one.', '400')
            return redirect("/CreateAccount")
        hashed_password = bcrypt.generate_password_hash(raw_password, 12).decode()
        # account_repository_singleton.create_account(username, email, hashed_password)
        new_user = Account(email, username, hashed_password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        if 'username' in session.keys():
            return redirect('/account')
        else:
            flash('Something went wrong.', 'Error')
            return redirect('/')
        # return redirect(f'/account/{created_account.Account.id}')
        # return render_template('Home_page.html', username=session['username'])
        # return redirect('/')
    else:
        return render_template("AccountCreation.html")
    
@app.route("/Login", methods = ["GET", "POST"])
def login_account():
    if request.method == "POST":
        username = request.form.get('User-Name')
        raw_password = request.form.get('User-Password')
        if not username or not raw_password:
            flash('All fields are required.', 'error')
            return render_template("Login.html")
        existing_user = Account.query.filter_by(username=username).first()
        if not existing_user:
            flash('The username does not exist. Please create an account first', 'error')
            return redirect('/CreateAccount')
        if not bcrypt.check_password_hash(existing_user.password, raw_password):
            flash('The password does not match. Please try again', 'error')
            return render_template("Login.html")
        # flash('Successfully logged in', 'success')
        session['username'] = username
        if 'username' in session:
            username = session['username']
            return redirect('/account')
        else:
            return redirect('/account')
    else:
        return render_template("Login.html")

@app.get("/Character")
def get_character():
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not character:
        return redirect('/CharacterCreation')
    if 'itemSearch' in request.args.keys():
        item_search = db_function.get_items_by_name(request.args.get('itemSearch'))
    else:
        item_search = None
    armor = db_function.get_item_data(character.armor)
    weapon = db_function.get_item_data(character.weapon)
    belt = db_function.get_item_data(character.belt)
    level = db_function.calc_level(character.experience)
    weight = db_function.inventory_weight(character)
    inventory = db_function.get_char_inventory(character)
    alignment = db_function.get_char_alignment(character)
    char_class = db_function.get_char_class(character)
    char_race = db_function.get_char_race(character)
    item_list = db_function.get_items()
    abilities = db_function.get_char_abilities(character)
    return render_template('Character.html', character = character, 
                           armor = armor, weapon = weapon, 
                           belt = belt, level = level, weight = weight, 
                           inventory = inventory, alignment = alignment,
                           char_class = char_class, char_race = char_race,
                           item_search = item_search, item_list = item_list, abilities = abilities)

@app.post("/Character")
def update_char():
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)

    if not character:
        flash('Character Not Found.', '404')
        return redirect('/')
    
    if 'hp' in request.form.keys():
        hp_change = request.form.get('hp')
    else:
        hp_change = None

    if 'item_add' in request.form.keys():
        item_add = request.form.get('item_add')
        if 'quantity' in request.form.keys():
            quantity = request.form.get('quantity')
        else:
            quantity = 1
    else:
        item_add = None

    if 'item_equip' in request.form.keys():
        item_equip = request.form.get('item_equip')
    else:
        item_equip = None

    if 'equipment' in request.form.keys():
        slot_remove = request.form.get('equipment')
    else:
        slot_remove = None

    if 'exp' in request.form.keys():
        exp = request.form.get('exp')
    else:
        exp = None

    if not item_add and not exp and not hp_change and not slot_remove and not item_equip:
        flash('Missing Input', '400')
        return redirect('/Character')
    
    if item_add:
        try:
            item_add = int(item_add)
            quantity = int(quantity)
        except:
            flash('Invalid input', '400')
            return redirect('/Character')
        if not db_function.get_item_data(item_add):
            flash('Item not Found', '404')
            return redirect('/Character')
        if 20+(character.grit*character.prowess/20) < db_function.inventory_weight(character) + db_function.get_item_data(item_add).weight * quantity:
            flash('To Much Weight', '400')
            return redirect('/Character')
        db_function.add_to_char_inv(item_add, character.id, quantity)
    
    if item_equip:
        try:
            item_equip = int(item_equip)
        except:
            flash('Invalid input', '400')
            return redirect('/Character')
        if not db_function.get_item_data(item_equip):
            flash('Item not Found', '404')
            return redirect('/Character')
        db_function.add_item_to_equip_slot(character, item_equip)
    
    if slot_remove:
        if slot_remove != 'weapon' and slot_remove != 'armor' and slot_remove != 'belt':
            flash('Invalid input', '400')
            return redirect('/Character')
        db_function.remove_item_in_equip_slot(character, slot_remove)
    
    if hp_change:
        try:
            hp_change = int(hp_change)
        except:
            flash('Invalid input', '400')
            return redirect('/Character')
        db_function.edit_character_hp(character, hp_change)
    
    if exp:
        try:
            exp = int(exp)
        except:
            flash('Invalid input', '400')
            return redirect('/Character')
        level = db_function.calc_level(character.experience)
        if level[0] < db_function.calc_level(character.experience + exp)[0]:
            db_function.add_exp(exp, character)
            return redirect('/LevelUp')
        else:
            db_function.add_exp(exp, character)
    return redirect('/Character')

@app.post("/Character/Delete")
def delete_character():
    if 'username' not in session:
        flash('User not in Session. Please Log in', 'Not_Authenticated 401')
        return redirect('/')
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if not character:
        flash('Character Not Found.', '404')
        return redirect('/')
    
    db_function.remove_character(character.id)
    return redirect('/')

@app.get("/feedback_page")
def get_feedback_page():
    return render_template('feedback_page.html')

@app.post('/logout')
def logout():
    del session['username']
    return redirect('/')

@app.route('/account')
def account():
    if "username" in session:
        username = session.get('username')
        email = db_function.get_email_from_username(session['username'])
        return render_template('Account.html', username=username, email=email)
    else:
        return redirect('/Login')

def delete_account(username):
    account = Account.query.filter_by(username=username).first()
    if account:
        db.session.delete(account)
        db.session.commit()
        return True
    else:
        return False

@app.route('/delete', methods = ['GET'])
def delete():
    username = session.get('username')
    if not username:
        flash('Username not found in session', '400')  
        return 'Username not found in session'
    account = db_function.get_account_id_from_username(session['username'])
    character = db_function.get_character_data(account)
    if character:
        db_function.remove_character(character.id)
    deletion_result = delete_account(username)
    if deletion_result:
        session.pop('username', None)
        flash('Account deleted successfully', 'message')
        return redirect('/')
    else:
        flash('Account failed to delete', '500')
        return redirect('/account')
    
@app.route('/update', methods=['GET', 'POST'])
def update_account():
    if request.method == 'POST':
        account_id = db_function.get_id_from_user(session['username'])
        if account_id:
            account = Account.query.filter_by(id=account_id).first()
            if account:
                account.username = request.form['username']
                account.email = request.form['email']
                db.session.commit()
                session['username'] = account.username
                return redirect('/account')
            else:
                flash('Account not found', '400')
                return 'Account not found'
        else:
            flash('Unable to update Account', '400')
            return 'Unable to update Account'
    else:
        username = session.get('username')
        email = db_function.get_email_from_username(session['username'])
        return render_template('updateAccount.html', username=username, email=email)
