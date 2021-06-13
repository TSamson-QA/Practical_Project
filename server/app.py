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
    alignment = requests.get('http://alignment_api:5003/get_alignment').text
    #alignment = "True Neutral"


    last_characters = Characters.query.order_by(desc(Characters.id)).limit(5).all()
    db.session.add(
        Characters(
            db_class_ = class_,
            db_race = race,
            db_alignment = alignment            

        )
    )

    db.session.commit()
        
    return render_template('index.html', gen_race=race, gen_class=class_, gen_alignment=alignment, last_characters=last_characters)



if __name__ == "__main__": app.run(host="0.0.0.0", port=5000, debug=True)