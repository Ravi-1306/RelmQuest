import datetime
from email.policy import default
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.sql.functions import current_date, now
from datetime import datetime

db = SQLAlchemy()

class Race(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(63), nullable = False)
    grt_mod = db.Column(db.Integer)
    prw_mod = db.Column(db.Integer)
    grc_mod = db.Column(db.Integer)
    wit_mod = db.Column(db.Integer)
    sav_mod = db.Column(db.Integer)

class Class(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(63), nullable = False)
    hp_mod = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)

class Country(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(63), nullable = False)

class Location(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    country = db.Column(db.Integer, db.ForeignKey('country.id'), nullable = False)

class Event(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    start_date = db.Column(db.Date, nullable = False)
    end_date = db.Column(db.Date, nullable = False)
    description = db.Column(db.Text, nullable = False)
    event_location = db.Column(db.BigInteger, db.ForeignKey('location.id'), nullable = False)

class Ability(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(63), nullable = False)
    description = db.Column(db.Text, nullable = False)
    level = db.Column(db.Integer, nullable = False)
    race_req = db.Column(db.Integer, db.ForeignKey('race.id'), nullable = True)
    class_req = db.Column(db.Integer, db.ForeignKey('class.id'), nullable = True)    

class Item(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    weight = db.Column(db.Float, nullable = False)
    equipable = db.Column(db.Boolean, nullable = False)
    damage = db.Column(db.Integer)
    armor = db.Column(db.Integer)

class Account(db.Model):
    id = db.Column(db.UUID,server_default=text("gen_random_uuid()"),  primary_key = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    username = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    # creation_date = db.Column(db.Date,server_default=current_date(), nullable = False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, username, password) -> None:
        self.email = email
        self.username = username
        self.password = password

class Character(db.Model):
    id = db.Column(db.UUID, server_default=text("gen_random_uuid()"), primary_key = True)
    account_id = db.Column(db.String(36), db.ForeignKey('account.id'), nullable = False)
    name = db.Column(db.String(63), nullable = False)
    race = db.Column(db.Integer, db.ForeignKey('race.id'), nullable = False)
    char_class = db.Column(db.Integer, db.ForeignKey('class.id'), nullable = False)
    experience = db.Column(db.BigInteger, nullable = False)
    creation_date = db.Column(db.Date,server_default=current_date(), nullable = False)
    location = db.Column(db.BigInteger, db.ForeignKey('location.id'), nullable = False)
    armor = db.Column(db.BigInteger, db.ForeignKey('item.id'))
    weapon = db.Column(db.BigInteger, db.ForeignKey('item.id'))
    belt = db.Column(db.BigInteger, db.ForeignKey('item.id'))
    grit = db.Column(db.Integer, nullable = False)
    prowess = db.Column(db.Integer, nullable = False)
    grace = db.Column(db.Integer, nullable = False)
    wit = db.Column(db.Integer, nullable = False)
    savvy = db.Column(db.Integer, nullable = False)
    cur_hp = db.Column(db.Integer, nullable = False)
    age = db.Column(db.Integer, nullable = False)
    religion = db.Column(db.String(255), nullable = False)
    personality = db.Column(db.Text)
    alignment = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text)
    backstory = db.Column(db.Text)
    image = db.Column(db.String)

class Chat_leungsaikok(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
    
class Chat_linshanho(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_peton(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_boton(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_trere(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_towbury(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_sobury(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_torkneth(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_alneridge(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_tarmouth(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)

class Chat_wigan(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_dhodh(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_ghoregag(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_dhezzol(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_gugh(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_cudadh(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
class Chat_arkorzaz(db.Model):
    id = db.Column(db.BigInteger, primary_key = True)
    account_id = db.Column(db.UUID, db.ForeignKey('account.id'), nullable = False)
    char_id = db.Column(db.UUID, db.ForeignKey('character.id'), nullable = False)
    time_stamp = db.Column(db.TIMESTAMP, server_default = now(), nullable = False)
    message = db.Column(db.TEXT, nullable = False)
    char_name = db.Column(db.String(63), nullable = False)
    profile_image = db.Column(db.String)
 
Char_ABLI = db.Table(
    'char_abli',
    db.Column('char_id', db.UUID, db.ForeignKey('character.id'), primary_key = True),
    db.Column('abli_id', db.BigInteger, db.ForeignKey('ability.id'), primary_key = True)
)

Char_INV = db.Table(
    'char_inv',
    db.Column('char_id', db.UUID, db.ForeignKey('character.id'), primary_key = True),
    db.Column('item_id', db.BigInteger, db.ForeignKey('item.id'), primary_key = True),
    db.Column('quantity', db.Integer, nullable = False)
)