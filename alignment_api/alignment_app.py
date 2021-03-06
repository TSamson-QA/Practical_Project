from typing import Text
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/get_alignment')
def get_alignment():
    class_ = requests.get('http://character_generator_class_api:5001/get_class').text
    race = requests.get('http://character_generator_race_api:5002/get_race').text

    class_dict = {'Cleric':1, 'Fighter':2, 'Bard':3, 'Monk':4, 'Druid':5, 'Sorcerer':6, 'Warlock':7, 'Rogue':8, 'Barbarian':9}
    race_dict = {'Dwarf':1, 'Halfling':2, 'Elf':3, 'Gnome':4, 'Human':5, 'Half-Elf':6, 'Tiefling':7, 'Dragonborn':8, 'Half-Orc':9}

    class_val = class_dict.get(class_)
    race_val = race_dict.get(race)

    align_value = round((class_val + race_val) / 2)
    
    alignment = {1:'Lawful Good', 2:'Neutral Good', 3:'Chaotic Good', 
    4:'Lawful Neutral', 5:'True Neutral', 6:'Chaotic Neutral', 
    7:'Lawful Evil', 8:'Neutral Evil', 9:'Chaotic Evil'}

    gen_alignment = alignment.get(align_value)

    return gen_alignment

if __name__ == "__main__": app.run(host="0.0.0.0", port=5003, debug=True)