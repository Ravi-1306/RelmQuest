from test.utils import clear_db
from src.models import db, Class, Race, Country, Location, Character, Account, Ability, Char_ABLI
from sqlalchemy import select
from app import session

def test_level_page_opens(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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

        response = test_app.get("/LevelUp")

        assert response.status_code == 200
        data = response.data.decode()
        assert '<h4 class = "ps-4 pt-1">Steve</h4>' in data
        assert '<button class="btn btn-dark" type="submit">Level Up!</button>' in data
        assert '<label class="form-check-label" for="none">No Ability</label>' in data

def test_level_up_post(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        ability = Ability(name = "FIREBALL 'MF'", 
                description = "blasts a firball at some enemies",
                level = 2,
                class_req = cl.id
                )
        db.session.add(ability)
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
                    name = "Steve",
                    race = race.id,
                    char_class = cl.id,
                    experience = 4000,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': f'{ability.id}'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert prev_grit != Character.query.filter_by(id = Steve.id).first().grit
        abil_connection = db.session.execute(select(Char_ABLI).where(Char_ABLI.c.char_id == Steve.id)).first().abli_id
        db.session.commit()
        assert ability.id == abil_connection

def test_level_up_post_without_ability(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert prev_grit != Character.query.filter_by(id = Steve.id).first().grit

def test_level_up_post_with_more_than_two(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '100554',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Too many Ability Increases' in response.data.decode()

def test_level_up_post_with_char_for_stat(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': 'a',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Savvy not Valid' in response.data.decode()

def test_level_up_post_with_unknown_ability(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '15'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Ability not Found' in response.data.decode()

def test_level_up_post_with_missing_input(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Grit not Valid' in response.data.decode()

def test_level_up_post_with_no_login(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post("/logout")
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
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        db.session.commit()
        Steve = Character(
                    account_id = Account.query.filter_by(username = 'LostInHere').first().id,
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
        prev_grit = Character.query.filter_by(id = Steve.id).first().grit
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'User not in Session. Please Log in.' in response.data.decode()

def test_level_up_post_with_no_character(test_app):
    with test_app.application.app_context():
        clear_db()
        test_app.post('/CreateAccount', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password',
            'User-Email': 'fired@example.com'
        })
        test_app.post('/Login', data={
            'User-Name': 'LostInHere',
            'User-Password': 'Password'
        })
        response = test_app.post("/LevelUp", data={
            'grit': '1',
            'prowess': '1',
            'grace': '0',
            'wit': '0',
            'savvy': '0',
            'ability': '0'
        }, follow_redirects = True)

        assert response.status_code == 200
        assert 'Character Not Found. Please create one.' in response.data.decode()