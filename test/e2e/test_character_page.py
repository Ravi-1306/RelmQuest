from src.models import Race, Country, Location, Class, Item
from csv_import import import_csv
from app import db

def test_character_page_opens(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.get('/Character', follow_redirects = True)
        data = response.data.decode()

        assert response.status_code == 200
        assert 'Steve' in data
        assert 'Chaotic Good' in data

def test_character_page_no_login(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        test_app.post('/logout')
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.get('/Character', follow_redirects = True)
        
        assert response.status_code == 200
        assert 'User not in Session. Please Log in' in response.data.decode()

def test_character_page_no_character(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        response = test_app.get('/Character', follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Character Creation' in response.data.decode()

def test_character_page_nodata(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', follow_redirects = True)
        data = response.data.decode()

        assert response.status_code == 200
        assert 'Missing Input' in data
        
def test_character_page_adding_item(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "arrow",
                    description = "Fired from a bow: with sharp end pointed to target...",
                    weight = .01,
                    equipable = False,
                    damage = 2
                    )
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_add' : item.id
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'arrow' in response.data.decode()

def test_character_page_adding_item_invalid(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_add' : 'g'
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Invalid input' in response.data.decode()

def test_character_page_item_notfound(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_add' : '420'
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Item not Found' in response.data.decode()

def test_character_page_weightlimit(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "Iron Block",
                    description = "Heavy Weight",
                    weight = 1800000,
                    equipable = False
                    )   
        db.session.add(item)
        db.session.commit()

        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_add' : item.id
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'To Much Weight' in response.data.decode()

def test_character_page_equip_item(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_equip' : item.id
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'sword Damage: 2' in response.data.decode()

def test_character_page_equip_invalid(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_equip' : 'g'
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Invalid input' in response.data.decode()

def test_character_page_equip_notfound(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'item_equip' : 420
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Item not Found' in response.data.decode()

def test_character_page_remove(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'weapon' : item.id,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'equipment' : 'weapon'
            }, follow_redirects = True)
        
        assert response.status_code == 200

def test_character_page_remove_invalid(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'weapon' : item.id,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'equipment' : 'hand'
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Invalid input' in response.data.decode()

def test_character_page_hp_change(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'hp' : -10
            }, follow_redirects = True)
        print(response.data.decode())

        assert response.status_code == 200
        assert f'{int((((18 - 10) / 4) + 5) * (cl.hp_mod / 100) - 10)}' in response.data.decode()

def test_character_page_hp_invalid(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'hp' : 'k'
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'Invalid input' in response.data.decode()

def test_character_page_exp(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'exp' : 100
            }, follow_redirects = True)
        
        assert response.status_code == 200
        assert 'aria-valuemax="300">100</div>' in response.data.decode()

def test_character_page_exp_invalid(test_app):
    with test_app.application.app_context():
        import_csv()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired'
        })
        
        race = Race(name = "GODBORN", grc_mod = 18, 
                            wit_mod = 18,
                            sav_mod = 18,
                            prw_mod = 18,
                            grt_mod = 18
                            )
        db.session.add(race)
        db.session.commit()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        cl = Class(name = "Merchant", hp_mod = 18, description = "steve... is steve")
        db.session.add(cl)
        db.session.commit()
        item = Item(name = "sword",
                    description = "pointy",
                    weight = 10,
                    equipable = True,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        test_app.post("/CharacterCreation", data ={ 
            'Character-Name' : 'Steve', 
            'Age' : 1000000000, 
            'Race' : race.id,
            'Alignment' : 3,
            'Personality' : 'Steve',
            'Religion' : 'Steve',
            'classSelect': cl.id,
            'equipmentSet' : 1,
            'stats1' : 18,
            'stats2' : 18,
            'stats3' : 18,
            'stats4' : 18,
            'stats5' : 18,
            'Backstorytxtbx': 'Steve ... is steve',
            'Descriptiontxtbx' : 'Steve ... looks like steve',
            'startingLocation' : country.id})
        
        response = test_app.post('/Character', data={
            'exp' : 'k'
            }, follow_redirects = True)
        data = response.data.decode()
        print(data)
        assert response.status_code == 200
        assert 'Invalid input' in response.data.decode()