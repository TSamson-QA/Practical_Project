from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_class')
def get_class():
    return random.choice(['Cleric', 'Fighter', 'Bard', 'Monk', 'Druid', 'Sorcerer', 'Warlock', 'Rogue', 'Barbarian'])
    #return random.choice({1:'Cleric', 2:'Fighter', 3:'Bard', 4:'Monk', 5:'Druid', 6:'Sorcerer', 7:'Warlock', 8:'Rogue', 9:'Barbarian'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)