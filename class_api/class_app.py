from flask import Flask
import random

app = Flask(__name__)

@app.route('/get_class')
def get_class():
    return random.choice(['Cleric', 'Fighter', 'Bard', 'Monk', 'Druid', 'Sorcerer', 'Warlock', 'Rogue', 'Barbarian'])

if __name__ == "__main__": app.run(host="0.0.0.0", port=5001, debug=True)