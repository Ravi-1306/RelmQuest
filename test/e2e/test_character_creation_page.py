import pytest
from test.utils import clear_db
from app import app, db
from csv_import import import_csv
from src.models import Character, Class, Race, Country, Location, Account
from sqlalchemy import insert, select

def test_Character_creation_opens(test_app):
    with test_app.application.app_context():    
        clear_db()
        test_app.post('/CreateAccount', data={
                'User-Name': 'LostInHere',
                'User-Password': 'Password',
                'User-Email': 'fired'
            })
        response = test_app.get("/CharacterCreation")
        assert response.status_code == 200

## need to extend test when database implemented
##test post request


def test_create_character(test_app):
    with test_app.application.app_context():
        import_csv()
        response = test_app.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password",
                        )
        db.session.add(account)
        db.session.commit()  

        db.session.add(Race(name = "ork", grc_mod = 2, wit_mod = 1))    
        db.session.commit()

        db.session.add(Class(name = "warrior", hp_mod = 6, description = "tanky" ))
        db.session.commit()
        
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        
        location =Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        


        response = test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'happy', 
            'Age' : 3, 
            'Race' : 1,
            'Alignment' : 3,
            'Personality' : 'happy',
            'Religion' : 'dead',
            'classSelect': 1,
            'equipmentSet' : 1,
            'stats1' : 1,
            'stats2' : 2,
            'stats3' : 3,
            'stats4' : 4,
            'stats5' : 5,
            'Backstorytxtbx': 'depreso',
            'Descriptiontxtbx' : 'cute',
            'startingLocation' : country.id}, follow_redirects = True)
        assert response.status_code == 200
        char = Character.query.first()
        assert char.name == 'happy'
        assert char.age == 3
        assert char.race == 1
        assert char.wit == 4
        assert char.description == 'cute'

def test_dif_create_character(test_app):
    with test_app.application.app_context():
        import_csv()
        response = test_app.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
        }, follow_redirects=True)
        
        assert response.status_code == 200

        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password",
                        )
        db.session.add(account)
        db.session.commit()  

        db.session.add(Race(name = "ork", grc_mod = 2, wit_mod = 1))    
        db.session.commit()

        db.session.add(Class(name = "warrior", hp_mod = 6, description = "tanky" ))
        db.session.commit()
        
        db.session.add(Class(name = "mage", hp_mod = 2, description = "fire" ))
        db.session.commit()

        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        
        location =Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        


        response = test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'sad', 
            'Age' : 7, 
            'Race' : 1,
            'Alignment' : 3,
            'Personality' : 'happy',
            'Religion' : 'dead',
            'classSelect': 2,
            'equipmentSet' : 1,
            'stats1' : 5,
            'stats2' : 4,
            'stats3' : 3,
            'stats4' : 2,
            'stats5' : 1,
            'Backstorytxtbx': 'depreso',
            'Descriptiontxtbx' : 'ugly',
            'startingLocation' : country.id}, follow_redirects = True)
        assert response.status_code == 200
        char = Character.query.first()
        assert char.name == 'sad'
        assert char.char_class == 2
        assert char.age == 7
        assert char.race == 1
        assert char.wit == 2
        assert char.description == 'ugly'


def test_inv_create_character(test_app):
    with test_app.application.app_context():
        import_csv()
        response = test_app.post('/CreateAccount', data={
        'User-Name': 'testuser',
        'User-Password': 'testpassword',
        'User-Email': 'test@example.com'
        }, follow_redirects=True)
        assert response.status_code == 200

        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password",
                        )
        db.session.add(account)
        db.session.commit()  

        db.session.add(Race(name = "ork", grc_mod = 2, wit_mod = 1))    
        db.session.commit()

        db.session.add(Class(name = "warrior", hp_mod = 6, description = "tanky" ))
        db.session.commit()
        
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        
        location =Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()

        response = test_app.post("/CharacterCreation", data ={ 
             
            'Age' : 3, 
            'Race' : 1,
            'Alignment' : 3,
            'Personality' : 'happy',
            'Religion' : 'dead',
            'classSelect': 1,
            'equipmentSet' : 1,
            'stats1' : 1,
            'stats2' : 2,
            'stats3' : 3,
            'stats4' : 4,
            'stats5' : 5,
            'Backstorytxtbx': 'depreso',
            'Descriptiontxtbx' : 'cute',
            'startingLocation' : country.id}, follow_redirects = True)
        assert  "please fill all fields" in response.data.decode()

