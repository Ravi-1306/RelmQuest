from src.models import Country, Race, Location, Ability, Item, Account, Character, Class, Event, Char_ABLI, Char_INV, Chat_alneridge, Chat_arkorzaz, Chat_boton, Chat_cudadh, Chat_dhezzol, Chat_dhodh, Chat_ghoregag, Chat_gugh, Chat_leungsaikok, Chat_linshanho, Chat_peton, Chat_tarmouth, Chat_torkneth, Chat_sobury, Chat_towbury, Chat_trere, Chat_wigan
from test.utils import clear_db
import datetime
from app import db
from sqlalchemy import insert, select

def test_country_model(test_app):
    with test_app.application.app_context():
        clear_db()
        db.session.add(Country(name = "alibaba"))
        db.session.commit()
        country = Country.query.first()
        assert country.name == "alibaba"

def test_race_model(test_app):
    with test_app.application.app_context():
        clear_db()
        db.session.add(Race(name = "elf", grc_mod = 2, wit_mod = 1))
        db.session.commit()
        race = Race.query.first()
        assert race.name == "elf"
        assert race.grc_mod == 2
        assert race.wit_mod == 1
        assert race.prw_mod == None

def test_class_model(test_app):
    with test_app.application.app_context():
        clear_db()
        wiz = Class(name = "Wizard", hp_mod = 2, description = "Fire boi")
        db.session.add(wiz)
        db.session.commit()
        clas = Class.query.first()
        assert clas.name == wiz.name
        assert clas.id == wiz.id
        assert clas.hp_mod == wiz.hp_mod

def test_location_model(test_app):
    with test_app.application.app_context():
        clear_db()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        place = Location.query.filter_by(id = location.id).first()
        assert place.name == "place"
        assert place.country == country.id

def test_event_model(test_app):
    with test_app.application.app_context():
        clear_db()
        country = Country(name = "alibaba")
        db.session.add(country)
        db.session.commit()
        location = Location(name = "place", country = country.id)
        db.session.add(location)
        db.session.commit()
        start_date = datetime.datetime(2020,10,15)
        end_date = datetime.datetime(2023,11,25)
        event = Event(name = "Dragon Flies Above", 
                      start_date = start_date,
                      end_date = end_date,
                      description = "The Dragon flies above the city and you can hear it's cries of pain and rage, will we soothe it or destroy it?",
                      event_location = location.id
                      )
        db.session.add(event)
        db.session.commit()
        test = Event.query.first()
        assert test.name == "Dragon Flies Above"
        assert test.event_location == location.id

def test_ability_model(test_app):
    with test_app.application.app_context():
        clear_db()
        race = Race(name = "elf", grc_mod = 2, wit_mod = 1)
        db.session.add(race)
        cl = Class(name = "Wizard", hp_mod = 2, description = "Fire boi")
        db.session.add(cl)
        db.session.commit()
        ability = Ability(name = "FIREBALL 'MF'", 
                description = "blasts a firball at some enemies",
                level = 2,
                class_req = cl.id
                )
        db.session.add(ability)
        db.session.commit()
        ability = Ability.query.first()
        assert ability.name == "FIREBALL 'MF'"
        assert ability.class_req == cl.id

def test_item_model(test_app):
    with test_app.application.app_context():
        clear_db()
        item = Item(name = "arrow",
                    description = "Fired from a bow: with sharp end pointed to target...",
                    weight = .01,
                    equipable = False,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        item = Item.query.first()
        assert item.name == "arrow"
        assert item.weight == .01
        assert item.equipable == False
        assert item.damage == 2


def test_account_model(test_app):
    with test_app.application.app_context():
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
        place = Account.query.first()
        assert place.username == "LostInHere"
        assert place.email == "fired"
        assert place.password == "Password"

def test_account_uniq(test_app):
    with test_app.application.app_context():
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        account2 = Account(email = "helo",
                        username = "LostInHere",
                        password = "Password"
                        )
        account3 = Account(email = "fired",
                        username = "scared being",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
        place = Account.query.first()
        assert place.username == "LostInHere"
        assert place.email == "fired"
        assert place.password == "Password"
        assert not db.session.add(account2)
        assert not db.session.add(account3)

def test_character_model(test_app):
    with test_app.application.app_context():
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
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
                    account_id = account.id,
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
        STEVE = Character.query.first()
        assert STEVE.name == "Steve"
        assert STEVE.experience == -1
        assert STEVE.alignment == 69

## Chat_Alneridge, Chat_Arkorzaz, Chat_Boton, Chat_Cudadh, Chat_Dhezzol, Chat_Dhodh, Chat_Ghoregag, Chat_Gugh, Chat_Leungsaikok, Chat_Linshanho, Chat_Peton, Chat_Tarmouth, Chat_Torkneth, Chat_Sobury, Chat_Towbury, Chat_Trere, Chat_Wigan
def test_chat_model(test_app):
    with test_app.application.app_context():    
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
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
                    account_id = account.id,
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
        chat = Chat_alneridge(
                    account_id = account.id,
                    char_id = Steve.id,
                    message = "Steve is the man. Steve has the pan. Steve cooks the flan.",
                    char_name = Steve.name,
                    profile_image = Steve.image
        )
        db.session.add(chat)
        db.session.commit()
        chat_log = Chat_alneridge.query.first()
        assert chat_log.id == chat.id
        assert chat_log.account_id == account.id
        assert chat_log.message == "Steve is the man. Steve has the pan. Steve cooks the flan."
        assert chat_log.profile_image == None


def test_char_abil_table(test_app):
    with test_app.application.app_context():
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
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
                    account_id = account.id,
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
        db.session.commit()
        db.session.add(Steve)
        db.session.commit()
        STEVE = Character.query.first()
        assert STEVE.name == "Steve"
        assert STEVE.experience == -1
        assert STEVE.alignment == 69
        ability = Ability(name = "FIREBALL 'MF'", 
                description = "blasts a firball at some enemies",
                level = 2,
                class_req = cl.id
                )
        db.session.add(ability)
        db.session.commit()
        db.session.execute(insert(Char_ABLI).values(char_id = Steve.id,
                        abli_id = ability.id
                        ))
        link = db.session.execute(select(Char_ABLI).where(Char_ABLI.c.char_id == Steve.id)).first()
        db.session.commit()
        assert link.abli_id == ability.id

def test_char_inv_table(test_app):
    with test_app.application.app_context():
        clear_db()
        account = Account(email = "fired",
                        username = "LostInHere",
                        password = "Password"
                        )
        db.session.add(account)
        db.session.commit()
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
                    account_id = account.id,
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
        db.session.commit()
        db.session.add(Steve)
        db.session.commit()
        STEVE = Character.query.first()
        assert STEVE.name == "Steve"
        assert STEVE.experience == -1
        assert STEVE.alignment == 69
        item = Item(name = "arrow",
                    description = "Fired from a bow: with sharp end pointed to target...",
                    weight = .01,
                    equipable = False,
                    damage = 2
                    )   
        db.session.add(item)
        db.session.commit()
        db.session.execute(insert(Char_INV).values(char_id = Steve.id,
                        item_id = item.id,
                        quantity = 500
                        ))
        link = db.session.execute(select(Char_INV).where(Char_INV.c.char_id == Steve.id)).first()
        db.session.commit()
        assert link.item_id == item.id
