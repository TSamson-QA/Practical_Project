from typing import Text
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    db_class_ = db.Column(db.String(20), nullable=False)
    db_race = db.Column(db.String(20), nullable=False)
    db_alignment = db.Column(db.String(20), nullable=False)

@app.route('/')
def home():
    class_ = requests.get('http://class_api:5001/get_class').text
    race = requests.get('http://race_api:5002/get_race').text
     
    class_dict = {'Cleric':1, 'Fighter':2, 'Bard':3, 'Monk':4, 'Druid':5, 'Sorcerer':6, 'Warlock':7, 'Rogue':8, 'Barbarian':9}
    race_dict = {'Dwarf':1, 'Halfling':2, 'Elf':3, 'Gnome':4, 'Human':5, 'Half-Elf':6, 'Tiefling':7, 'Dragonborn':8, 'Half-Orc':9}

    class_val = class_dict.get(class_)
    race_val = race_dict.get(race)

    align_value = round((class_val + race_val) / 2)
    
    alignment = {1:'Lawful Good', 2:'Neutral Good', 3:'Chaotic Good', 
    4:'Lawful Neutral', 5:'True Neutral', 6:'Chaotic Neutral', 
    7:'Lawful Evil', 8:'Neutral Evil', 9:'Chaotic Evil'}

    gen_alignment = alignment.get(align_value)

    last_characters = Characters.query.order_by(desc(Characters.id)).limit(5).all()
    db.session.add(
        Characters(
            db_class_ = class_,
            db_race = race,
            db_alignment = gen_alignment
            
        )
    )

    db.session.commit()
        
    return render_template('index.html', gen_race=race, gen_class=class_, gen_alignment=gen_alignment, last_characters=last_characters)



if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)