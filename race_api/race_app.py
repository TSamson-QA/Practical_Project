from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_race')
def get_race():
    #randomly gets values from set list.
    return random.choice(['Dwarf', 'Halfling', 'Elf', 'Gnome', 'Human', 'Half-Elf', 'Tiefling', 'Dragonborn', 'Half-Orc'])
   

if __name__ == "__main__": app.run(host="0.0.0.0", port=5002, debug=True)