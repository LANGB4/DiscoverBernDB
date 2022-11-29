from flask import Blueprint, render_template, jsonify
from database import Bundeshaus


views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the home page!'  )

@views.route('/detail/<sightname>')
def detail(sightname):
    return render_template('index.html', info = 'here you see the detailed view of ' + sightname)


Kindlifresserbrunnen = {'name': 'Kindlifresserbrunnen',
                        'address': "Kornhausplatz 18",
                        'buss top': 'Zytglogge',
                        'Description': 'Die Brunnenfigur ist eine'
                                        'auf ein Postament lehnende Kinderschreckfigur'
                                        ' (Kinderfresser, im Englischen Oger), die gerade'
                                        ' ein nacktes Kind verschlingt. In einem umgehängten '  
                                        'Sack befinden sich weitere Kinder. Der Kinderfresser '
                                        'trägt einen spitzen Hut mit eingerollter Krempe.'
                        }


@views.route('/json')
def get_json():
    return jsonify(Bundeshaus)

