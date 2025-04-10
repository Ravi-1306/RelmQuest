from src.models import db, Country, Race, Location, Event, Ability, Item, Account, Character, Class, Char_ABLI, Char_INV
from sqlalchemy import func, Table, MetaData, select, insert

## if you need to operate on the database put your methods here
class db_actions:

    def get_all_users(self):
        return Account.query.all()

    def get_user_by_email(self, email):
        return Account.query.get(email)
    
    def get_user_by_username(self, username):
        return Account.query.get(username)
    
    def get_id_from_user(self, username):
        account = Account.query.filter_by(username=username).first()
        if account:
            return account.id
        return None

    def get_account_id_from_username(self, username):
        return Account.query.filter_by(username = username).first().id
    
    def get_email_from_username(self, username):
        account = Account.query.filter_by(username=username).first()
        if account:
            return account.email
        return None
        # return Account.query.filter_by(username=username).first().email

    def create_account(self, username, email, password):
        account = Account(email, username, password)
        db.session.add(account)
        db.session.commit()
        return account
    
    def search_accounts(self, email):
        return Account.query.filter(func.lower(Account.email).ilike(f"%{email}%")).all()
    
    def get_character_data(self, account_id):
        return Character.query.filter_by(account_id = account_id).first()
    
    def get_item_data(self, item_id):
        return Item.query.filter_by(id = item_id).first()
    
    def get_items_by_name(self, item):
        return Item.query.filter(Item.name.ilike(f"%{item}%")).all()
    
    def get_items(self):
        return Item.query.all()
    
    def get_races(self):
        return Race.query.all()
    
    def get_classes(self):
        return Class.query.all()
    
    def calc_level(self,exp):
        if (exp < 300):
            return (1,0,300)
        elif  (exp < 900):
            return (2,300,900)
        elif (exp < 2700):
            return (3,900,2700)
        elif (exp < 6500):
            return (4,2700,6500)
        elif (exp < 14_000):
            return (5,6500,14_000)
        elif (exp < 23_000):
            return (6,14_000,23_000)
        elif (exp < 34_000):
            return (7,23_000,34_000)
        elif (exp < 48_000):
            return (8,34_000,48_000)
        elif (exp < 64_000):
            return (9,48_000,64_000)
        elif (exp < 85_000):
            return (10,64_000,85_000)
        elif (exp < 100_000):
            return (11,85_000,100_000)
        elif (exp < 120_000):
            return (12,100_000,120_000)
        elif (exp < 140_000):
            return (13,120_000,140_000)
        elif (exp < 165_000):
            return (14,140_000,165_000)
        elif (exp < 195_000):
            return (15,165_000,195_000)
        elif (exp < 225_000):
            return (16,195_000,225_000)
        elif (exp < 265_000):
            return (17,225_000,265_000)
        elif (exp < 305_000):
            return (18,265_000,305_000)
        elif (exp < 355_000):
            return (19,305_000,355_000)
        else:
            return (20,355_000,355_000)
    
    def inventory_weight(self,c):
        inv = db.session.execute(select(Char_INV).where(Char_INV.c.char_id == c.id)).all()
        weight = 0
        for x in inv:
            item = Item.query.filter_by(id = x.item_id).first()
            weight += item.weight * x.quantity
            print(weight)
        return weight
    
    def get_char_inventory(self,c):
        inv_q = db.session.execute(select(Char_INV).where(Char_INV.c.char_id == c.id)).all()
        inv = []
        for x in inv_q:
            item = Item.query.filter_by(id = x.item_id).first()
            inv.append((item, x.quantity))
        return inv
    
    def get_char_abilities(self,c):
        ability_q = db.session.execute(select(Char_ABLI).where(Char_ABLI.c.char_id == c.id)).all()
        abilities = []
        for x in ability_q:
            ability = Ability.query.filter_by(id = x.abli_id).first()
            abilities.append(ability)
        return abilities
    
    def get_char_alignment(self,c):
        alignment = c.alignment
        match alignment:
            case 1:
                return 'Lawful Good'
            case 2:
                return 'Neutral Good'
            case 3:
                return 'Chaotic Good'
            case 4:
                return 'Lawful Neutral'
            case 5:
                return 'Neutral'
            case 6:
                return 'Chaotic Neutral'
            case 7:
                return 'Lawful Evil'
            case 8:
                return 'Neutral Evil'
            case 9:
                return 'Chaotic Evil'
            case 69:
                return 'Ruler of the Universe, Divine One. Dark Overlord of the Forgotten Places, Dark One'
            case _:
                return 'HONK'
    
    def get_char_class(self,c):
        return Class.query.filter_by(id = c.char_class).first()
    
    def get_class(self, class_id):
        return Class.query.filter_by(id = class_id).first()

    def get_race(self, race_id):
        return Race.query.filter_by(id = race_id).first()

    def get_char_race(self,c):
        return Race.query.filter_by(id = c.race).first().name
    
    def edit_character_hp(self, character, hp_edit):
        character = Character.query.filter_by(id = character.id).first()
        setattr(character, 'cur_hp', character.cur_hp + hp_edit)
        db.session.commit()

    def remove_character(self, character_id):
        locations = Location.query.all()
        for location in locations: 
            self.remove_city_messages_for_character(location.name, character_id)
        db.session.execute(Char_ABLI.delete().where(Char_ABLI.c.char_id == character_id))
        db.session.execute(Char_INV.delete().where(Char_INV.c.char_id == character_id))
        character = Character.query.filter_by(id = character_id).first()
        db.session.delete(character)
        db.session.commit()
    
    def add_to_char_inv(self, item, char_id, quantity):
        item_pair = db.session.query(Char_INV).filter_by(char_id = char_id, item_id = item).first()
        if item_pair:    
            db.session.query(Char_INV).filter_by(char_id = char_id, item_id = item).\
                        update({'quantity' : item_pair.quantity + quantity})
            item_pair = db.session.query(Char_INV).filter_by(char_id = char_id, item_id = item).first()
            if item_pair.quantity  <= 0:
                db.session.execute(Char_INV.delete().where(Char_INV.c.char_id == char_id, Char_INV.c.item_id == item))
        else:
            db.session.execute(insert(Char_INV).values(char_id = char_id,
                        item_id = item,
                        quantity = quantity
                        ))
        db.session.commit()
    
    def add_item_to_equip_slot(self, character, item_id):
        if character.weapon is None:
            setattr(character, 'weapon', item_id)
            self.add_to_char_inv(item_id, character.id, -1)
            db.session.commit()
        elif character.armor is None:
            setattr(character, 'armor', item_id)
            self.add_to_char_inv(item_id, character.id, -1)
            db.session.commit()
        elif character.belt is None:
            setattr(character, 'belt', item_id)
            self.add_to_char_inv(item_id, character.id, -1)
            db.session.commit()
        else:
            return False
    
    def remove_item_in_equip_slot(self, character, equip_slot):
        match equip_slot:
            case 'weapon':
                item = self.get_item_data(character.weapon)
            case 'armor':
                item = self.get_item_data(character.armor)
            case 'belt':
                item = self.get_item_data(character.belt)
            case _:
                return
        if item:    
            setattr(character, equip_slot, None)
            self.add_to_char_inv(item.id, character.id, 1)
            db.session.commit()
    
    def add_exp(self, exp, character):
        character.experience += exp
        db.session.commit()
        return character.experience
    
    def get_hp_mod(self, class_id):
        return Class.query.filter_by(id = class_id).first().hp_mod
    
    ## the user id
    ## the image    
    def make_Character(self, user_id,character_Name, character_Age, character_Race, character_Alignment, character_Personality, character_Religion, 
                       character_Class, character_Grit, character_Prowess, character_Grace, character_Wit, character_Savvy,
                       character_Backstory, character_Descriptiontxtbx, character_StartingLocation, image_filename):
        new_character = Character(account_id = user_id, name = character_Name, race = character_Race, char_class = character_Class, 
                              experience = 0, location = character_StartingLocation, grit = character_Grit, 
                              wit = character_Wit, prowess = character_Prowess, grace = character_Grace, 
                              savvy = character_Savvy,
                              cur_hp = int((((character_Grit - 10) / 4) + 5) * (self.get_hp_mod(character_Class)/100)), 
                              age = character_Age, religion = character_Religion, alignment = character_Alignment, 
                              description = character_Descriptiontxtbx, backstory =  character_Backstory, personality = character_Personality, image = image_filename)
        db.session.add(new_character)
        db.session.commit()
        return new_character
    
    def get_city(self, name):
        return Location.query.filter_by(name = name).first()
    
    def get_all_events_for_city(self, city_id :int):
        return Event.query.filter_by(event_location = city_id).all()
    
    def get_city_message(self, city_name, message_id):
        metadata_obj = MetaData()
        message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        message = db.session.query(message_table).filter_by(id= message_id).first()
        return message
    
    def get_city_messages_50(self, city_name: str):
        metadata_obj = MetaData()
        try:
            message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        except:
            return []
        messages = db.session.query(message_table).order_by(message_table.c.time_stamp.desc()).limit(50)
        messages = messages[::-1]
        return messages
    
    def insert_city_message(self, message, character_id, account_id, char_name, mess_image, city_name):
        metadata_obj = MetaData()
        message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        
        result = db.session.execute(message_table.insert().values(
            char_id = character_id,
            account_id = account_id,
            message = message,
            char_name = char_name, 
            profile_image = mess_image
        ).returning(message_table.c.id))
        db.session.commit()
        return result.fetchone().id
        
    def remove_city_message(self, city_name, message):
        metadata_obj = MetaData()
        message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        db.session.execute(message_table.delete().where(message_table.c.id == message.id))
        db.session.commit()
    
    def remove_city_messages_for_character(self, city_name, char_id):
        metadata_obj = MetaData()
        message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        db.session.execute(message_table.delete().where(message_table.c.char_id == char_id))
        db.session.commit()

    def edit_city_message(self, message_id, city_name, message_change):
        metadata_obj = MetaData()
        message_table = Table(f"chat_{city_name.lower()}", metadata_obj, autoload_with = db.engine)
        db.session.query(message_table).filter_by(id = message_id).update\
            ({'message': message_change})
        db.session.commit()
    
    def get_character_data_by_char_id(self, char_id):
        return Character.query.filter_by(id = char_id).first()
    
    def get_abilities_for_level(self, level, race, char_class):
        level_num = level[0]
        abils_class = Ability.query.filter_by(class_req = char_class, level = level_num).all()
        abils_race = Ability.query.filter_by(race_req = race, level = level_num).all()
        abils = abils_class + abils_race
        return abils
    
    def get_ability(self, ability_id):
        return Ability.query.filter_by(id = ability_id).first()

    def level_character(self, character, ability_id, grit_mod, prowess_mod, grace_mod, wit_mod, savvy_mod):
        if ability_id != 0:
            db.session.execute(insert(Char_ABLI).values(char_id = character.id,
                        abli_id = ability_id
                        ))
            db.session.commit()
        db.session.query(Character).filter_by(id = character.id).update\
                                ({'grit': character.grit + grit_mod,
                                  'prowess': character.prowess + prowess_mod,
                                  'grace': character.grace + grace_mod,
                                  'wit': character.wit + wit_mod,
                                  'savvy': character.savvy + savvy_mod
                                })
        db.session.commit()

    def add_equipment_set(self, set_num, character):
        match set_num:
            case 1: 
                self.add_to_char_inv(3,character.id,1)
                self.add_to_char_inv(14,character.id,1)
                self.add_to_char_inv(34,character.id,1)
            case 2:
                self.add_to_char_inv(8,character.id,1)
                self.add_to_char_inv(35,character.id,1)
                self.add_to_char_inv(32,character.id,1)
            case 3:
                self.add_to_char_inv(7,character.id,1)
                self.add_to_char_inv(35,character.id,1)
                self.add_to_char_inv(33,character.id,1)
            case 4:
                self.add_to_char_inv(10,character.id,1)
                self.add_to_char_inv(2,character.id,1)
                self.add_to_char_inv(19,character.id,1)
            case 5:
                self.add_to_char_inv(7,character.id,1)
                self.add_to_char_inv(2,character.id,1)
                self.add_to_char_inv(37,character.id,1)
            case _:
                self.add_to_char_inv(1,character.id,1)
                self.add_to_char_inv(31,character.id,1)
                self.add_to_char_inv(9,character.id,1)

    def add_first_ability(self, char_class, character):
        ability = Ability.query.filter_by(class_req = char_class, level = 1).first()
        if ability:
            db.session.execute(insert(Char_ABLI).values(char_id = character.id,
                        abli_id = ability.id
                        ))
            db.session.commit()

    def add_equipment_set(self, set_num, character):
        match set_num:
            case 1: 
                self.add_to_char_inv(3,character.id,1)
                self.add_to_char_inv(14,character.id,1)
                self.add_to_char_inv(34,character.id,1)
            case 2:
                self.add_to_char_inv(8,character.id,1)
                self.add_to_char_inv(35,character.id,1)
                self.add_to_char_inv(32,character.id,1)
            case 3:
                self.add_to_char_inv(7,character.id,1)
                self.add_to_char_inv(35,character.id,1)
                self.add_to_char_inv(33,character.id,1)
            case 4:
                self.add_to_char_inv(10,character.id,1)
                self.add_to_char_inv(2,character.id,1)
                self.add_to_char_inv(19,character.id,1)
            case 5:
                self.add_to_char_inv(7,character.id,1)
                self.add_to_char_inv(2,character.id,1)
                self.add_to_char_inv(37,character.id,1)
            case _:
                self.add_to_char_inv(1,character.id,1)
                self.add_to_char_inv(31,character.id,1)
                self.add_to_char_inv(9,character.id,1)

    def add_first_ability(self, char_class, character):
        ability = Ability.query.filter_by(class_req = char_class, level = 1).first()
        if ability:
            db.session.execute(insert(Char_ABLI).values(char_id = character.id,
                        abli_id = ability.id
                        ))
            db.session.commit()

    def get_country(self, country_name):
        return Country.query.filter_by(name= country_name).first()

    def get_location_by_country(self, country_id):
        return Location.query.filter_by(country= country_id).all()

#to be used in other modules
db_function = db_actions()

