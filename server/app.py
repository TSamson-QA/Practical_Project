from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    class_ = requests.get('http://class_api:5000/get_class')
    race = requests.get('http://race_api:5000/get_race')
    gen_class = class_.value()
    gen_race = race.value() 

    align_value = round((int(class_.key) * int(race.key)) / 2)

    alignment = {1:'Lawful Good', 2:'Neutral Good', 3:'Chaotic Good', 
    4:'Lawful Neutral', 5:'True Neutral', 6:'Chaotic Neutral', 
    7:'Lawful Evil', 8:'Neutral Evil', 9:'Chaotic Evil'}

    gen_alignment = alignment.value(align_value)


    
    return render_template('index.html', gen_race=gen_race, gen_class=gen_class, gen_alignment=gen_alignment)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)