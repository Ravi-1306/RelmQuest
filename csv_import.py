#Modify this for each different table you will be entering data in
#Place your csv file in
from src.models import db, Item, Country, Location, Race, Class, Ability
import csv
from test.utils import clear_db
from app import app
from sqlalchemy import text
from test.utils import clear_db

def import_csv():
    with app.app_context():
        clear_db()

        #copy this
        with open('static/import_csv/items.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['Name'])
                des = str(line['Description'])
                w = float(line['Weight'])
                if line['Equipable'] == 'TRUE':
                    e = True
                else:
                    e = False
                if line['Damage'] == '':
                    dam = None
                else:
                    dam = int(line['Damage'])
                if line['Armor'] == '':
                    a = None
                else:
                    a = int(line['Armor'])
                #print(line)
                new_item = Item(name = n, description = des, weight = w, equipable = e, damage = dam, armor = a)
                #print(new_item.name)
                db.session.add(new_item)
                db.session.commit()
        file.close()
        
        with open('static/import_csv/countries.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['Name'])
                
                new_country = Country(name = n)
                db.session.add(new_country)
                db.session.commit()
        file.close()

        with open('static/import_csv/locations.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['Name'])
                c = str(line['Country'])            
                new_country = Location(name = n, country = c)
                db.session.add(new_country)
                db.session.commit()
        file.close()

        with open('static/import_csv/races.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['name'])
                g = int(line['grt_mod'])            
                p = int(line['prw_mod'])            
                gr = int(line['grc_mod'])            
                w = int(line['wit_mod'])            
                s = int(line['sav_mod'])            
                new_race = Race(name = n, grt_mod = g, prw_mod = p, 
                                grc_mod = gr, wit_mod = w, sav_mod = s)
                db.session.add(new_race)
                db.session.commit()
        file.close()

        with open('static/import_csv/classes.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['name'])
                h = int(line['hp_mod'])
                d = str(line['description'])
                new_class = Class(name = n, hp_mod = h, description = d)
                db.session.add(new_class)
                db.session.commit()
        file.close()

        with open('static/import_csv/abilities.csv', mode = 'r') as file:
            csvFile = csv.DictReader(file) #used this so column heads 
            for line in csvFile:
                n = str(line['name'])
                d = str(line['description'])
                r = str(line['race_req'])
                c = str(line['class_req'])
                l = int(line['level'])
                if r == 'NULL':
                    r = None
                if c == 'NULL':
                    c == None
                new_ability = Ability(name = n, description = d, race_req = r, 
                                    class_req = c, level = l)
                db.session.add(new_ability)
                db.session.commit()
        file.close()

import_csv()