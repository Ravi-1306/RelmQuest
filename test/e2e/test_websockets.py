from src.models import Country, Race, Location, Character, Class
from test.utils import clear_db
from src.db_actions import db_function
from flask_socketio import rooms
from sqlalchemy import Table, MetaData
from app import app, db, socketio, users_on_location

def test_websocket_connection(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
        })

        account = db_function.get_account_id_from_username("LostInHere")
        race = Race(name = "GODBORN", grc_mod = 2000000000, 
                            wit_mod = 2000000000,
                            sav_mod = 2000000000,
                            prw_mod = 2000000000,
                            grt_mod = 2000000000
                            )
        db.session.add(race)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 2000000000, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Alneridge", country = country.id)
        db.session.add(location)
        db.session.commit()
        Steve = Character(
                    account_id = account,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = -1,
                    location = location.id,
                    grit = 2000000000,
                    prowess = 2000000000,
                    grace = 2000000000,
                    wit = 2000000000,
                    savvy = 2000000000,
                    cur_hp = 2000000000,
                    age = 1000000000,
                    alignment = 69
        )
        db.session.add(Steve)
        db.session.commit()
        test_app.get('/Location/Alneridge')
        test_socket = socketio.test_client(app,  flask_test_client= test_app)
        test_socket.connect()
        test_socket.emit('connection', 'Alneridge')

        assert ("Steve", None) in users_on_location['Alneridge']

def test_websocket_disconnection(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
        })

        account = db_function.get_account_id_from_username("LostInHere")
        race = Race(name = "GODBORN", grc_mod = 2000000000, 
                            wit_mod = 2000000000,
                            sav_mod = 2000000000,
                            prw_mod = 2000000000,
                            grt_mod = 2000000000
                            )
        db.session.add(race)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 2000000000, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Alneridge", country = country.id)
        db.session.add(location)
        db.session.commit()
        Steve = Character(
                    account_id = account,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = -1,
                    location = location.id,
                    grit = 2000000000,
                    prowess = 2000000000,
                    grace = 2000000000,
                    wit = 2000000000,
                    savvy = 2000000000,
                    cur_hp = 2000000000,
                    age = 1000000000,
                    alignment = 69
        )
        db.session.add(Steve)
        db.session.commit()
        test_app.get('/Location/Alneridge')
        test_socket = socketio.test_client(app,  flask_test_client= test_app)
        test_socket.connect()
        test_socket.emit('connection', 'Alneridge')
        assert ("Steve", None) in users_on_location['Alneridge']
        test_socket.disconnect()
        assert ("Steve", None) not in users_on_location['Alneridge']

def test_websocket_handle_message(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
        })

        account = db_function.get_account_id_from_username("LostInHere")
        race = Race(name = "GODBORN", grc_mod = 2000000000, 
                            wit_mod = 2000000000,
                            sav_mod = 2000000000,
                            prw_mod = 2000000000,
                            grt_mod = 2000000000
                            )
        db.session.add(race)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 2000000000, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Alneridge", country = country.id)
        db.session.add(location)
        db.session.commit()
        Steve = Character(
                    account_id = account,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = -1,
                    location = location.id,
                    grit = 2000000000,
                    prowess = 2000000000,
                    grace = 2000000000,
                    wit = 2000000000,
                    savvy = 2000000000,
                    cur_hp = 2000000000,
                    age = 1000000000,
                    alignment = 69
        )
        db.session.add(Steve)
        db.session.commit()
        test_app.get('/Location/Alneridge')
        test_socket = socketio.test_client(app,  flask_test_client= test_app)
        test_socket.connect()
        test_socket.emit('connection', 'Alneridge')
        test_socket.emit('message_sent', 'Steve is .... steve', 'Alneridge')

        metadata_obj = MetaData()
        message_table = Table("chat_alneridge", metadata_obj, autoload_with = db.engine)
        assert 'Steve is .... steve' == db.session.query(message_table).filter_by(char_id = Steve.id).first().message

def test_city_message_edit(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
        })

        account = db_function.get_account_id_from_username("LostInHere")
        race = Race(name = "GODBORN", grc_mod = 2000000000, 
                            wit_mod = 2000000000,
                            sav_mod = 2000000000,
                            prw_mod = 2000000000,
                            grt_mod = 2000000000
                            )
        db.session.add(race)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 2000000000, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Alneridge", country = country.id)
        db.session.add(location)
        db.session.commit()
        Steve = Character(
                    account_id = account,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = -1,
                    location = location.id,
                    grit = 2000000000,
                    prowess = 2000000000,
                    grace = 2000000000,
                    wit = 2000000000,
                    savvy = 2000000000,
                    cur_hp = 2000000000,
                    age = 1000000000,
                    alignment = 69
        )
        db.session.add(Steve)
        db.session.commit()
        test_app.get('/Location/Alneridge')
        test_socket = socketio.test_client(app,  flask_test_client= test_app)
        test_socket.connect()
        test_socket.emit('connection', 'Alneridge')
        test_socket.emit('message_sent', 'Steve is .... steve', 'Alneridge')
        metadata_obj = MetaData()
        message_table = Table("chat_alneridge", metadata_obj, autoload_with = db.engine)
        message_id = db.session.query(message_table).filter_by(char_id = Steve.id).first().id
        response = test_app.post('/Location/Alneridge', data = {
                'message_id' : message_id,
                'message' : 'Steve is............STEVE!!!!?!'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Steve is............STEVE!!!!?!' == db.session.query(message_table).filter_by(char_id = Steve.id).first().message

def test_city_message_delete(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/Login', data={
        'User-Name': 'LostInHere',
        'User-Password': 'Password'
        })

        account = db_function.get_account_id_from_username("LostInHere")
        race = Race(name = "GODBORN", grc_mod = 2000000000, 
                            wit_mod = 2000000000,
                            sav_mod = 2000000000,
                            prw_mod = 2000000000,
                            grt_mod = 2000000000
                            )
        db.session.add(race)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 2000000000, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Alneridge", country = country.id)
        db.session.add(location)
        db.session.commit()
        Steve = Character(
                    account_id = account,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = -1,
                    location = location.id,
                    grit = 2000000000,
                    prowess = 2000000000,
                    grace = 2000000000,
                    wit = 2000000000,
                    savvy = 2000000000,
                    cur_hp = 2000000000,
                    age = 1000000000,
                    alignment = 69
        )
        db.session.add(Steve)
        db.session.commit()
        test_app.get('/Location/Alneridge')
        test_socket = socketio.test_client(app,  flask_test_client= test_app)
        test_socket.connect()
        test_socket.emit('connection', 'Alneridge')
        test_socket.emit('message_sent', 'Steve is .... steve', 'Alneridge')
        metadata_obj = MetaData()
        message_table = Table("chat_alneridge", metadata_obj, autoload_with = db.engine)
        message_id = db.session.query(message_table).filter_by(char_id = Steve.id).first().id
        response = test_app.post('/Location/Alneridge/delete', data = {
            'message_id' : message_id
        }, follow_redirects = True)
        
        assert response.status_code == 200
        assert None == db.session.query(message_table).filter_by(char_id = Steve.id).first()