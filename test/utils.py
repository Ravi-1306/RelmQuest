from src.models import db, Country, Race, Location, Ability, Item, Account, Character, Class, Char_ABLI, Char_INV, Event, Chat_alneridge, Chat_arkorzaz, Chat_boton, Chat_cudadh, Chat_dhezzol, Chat_dhodh, Chat_ghoregag, Chat_gugh, Chat_leungsaikok, Chat_linshanho, Chat_peton, Chat_tarmouth, Chat_torkneth, Chat_sobury, Chat_towbury, Chat_trere, Chat_wigan
from sqlalchemy import text
from app import app

def clear_db():
    db.session.execute(Char_ABLI.delete())
    db.session.execute(Char_INV.delete())
    Chat_arkorzaz.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_arkorzaz_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_alneridge.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_alneridge_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_boton.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_boton_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_cudadh.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_cudadh_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_dhezzol.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_dhezzol_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_dhodh.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_dhodh_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_ghoregag.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_ghoregag_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_gugh.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_gugh_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_linshanho.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_linshanho_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_leungsaikok.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_leungsaikok_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_peton.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_peton_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_sobury.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_sobury_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_tarmouth.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_tarmouth_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_torkneth.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_torkneth_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_towbury.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Chat_towbury_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_trere.query.delete()   
    reset_sequence_sql = f"ALTER SEQUENCE Chat_trere_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Chat_wigan.query.delete()   
    reset_sequence_sql = f"ALTER SEQUENCE Chat_wigan_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Character.query.delete()
    Account.query.delete()
    Ability.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Ability_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Event.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Event_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Location.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Location_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Country.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Country_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Race.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Race_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Class.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Class_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    Item.query.delete()
    reset_sequence_sql = f"ALTER SEQUENCE Item_id_seq RESTART WITH 1;"
    db.session.execute(text(reset_sequence_sql))
    db.session.commit()