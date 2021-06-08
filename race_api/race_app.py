from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_race')
def get_race():
    #randomly gets values from set list.
    return random.choice({1:'Dwarf', 2:'Halfling', 3:'Elf', 4:'Gnome', 5:'Human', 6:'Half-Elf', 7:'Tiefling', 8:'Dragonborn', 9:'Half-Orc'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)