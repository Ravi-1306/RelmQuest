from src.models import Country, Race, Location, Character, Class
from test.utils import clear_db
from src.db_actions import db_function
from flask import get_flashed_messages
from app import db

def test_city_page_opens(test_app):
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
        location = Location(name = "Test_City", country = country.id)
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

        response = test_app.get("/Location/Test_City")
        assert response.status_code == 200
        data = response.data.decode()
        assert 'Test_City' in data
        assert '/static/assets/notice_board.jpg' in data
        assert str('<div class = "row p-2 vh-100" style = "background-image: url(/static/assets/towns/Test_City.png); background-size: cover">') in data

def test_city_page_no_login(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/logout')
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
        location = Location(name = "Test_City", country = country.id)
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
        response = test_app.get("/Location/Test_City", follow_redirects = True)
        assert 'User not in Session. Please Log in.' in response.data.decode()

def test_city_page_no_city(test_app):
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
        location = Location(name = "Test_City", country = country.id)
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

        response = test_app.get("/Location/Al'sTheator", follow_redirects = True)
        assert 'Location not Found.' in response.data.decode() 

def test_city_page_no_character(test_app):
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

        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "Test_City", country = country.id)
        db.session.add(location)
        db.session.commit()
        
        response = test_app.get("/Location/Test_City", follow_redirects = True)
        assert 'Character Not Found. Please create one.' in response.data.decode()