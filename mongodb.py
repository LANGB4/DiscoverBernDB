from pymongo import MongoClient
from bson import ObjectId
from flask import Blueprint, render_template, jsonify, request, redirect


client = MongoClient('localhost', 27017)

DiscoBern = client.DiscoBern

Kindlifresserbrunnen = {'name': 'Kindlifresserbrunnen',
                        'address': "Kornhausplatz 18",
                        'buss top': 'Zytglogge',
                        'Description': 'Die Brunnenfigur ist eine auf ein Postament '
                                       'lehnende Kinderschreckfigur (Kinderfresser, im Englischen Oger), '
                                       'die gerade ein nacktes Kind verschlingt. In einem umgehängten '
                                       'Sack befinden sich weitere Kinder. Der Kinderfresser trägt einen spitzen '
                                       'Hut mit eingerollter Krempe.'
                        }

Rosengarten = {'name': 'Rosengarten',
               'address': "Alter Argauerstalden 31B",
               'buss top': 'Rosengarten',
               'Description': 'Der Rosengarten gehört zu den schönsten Parks'
                              'der Stadt Bern und bietet einen einmaligen Blick'
                              'auf die Dachlandschaft der historischen Altstadt,'
                              'das Münster und die Aareschlaufe. '
               }

Bundeshaus = {'name': 'Bundeshaus',
              'address': "Bundesplatz 3",
              'buss top': 'Bundesplatz',
              'Description': 'Als Bundeshaus wird der Sitz von Regierung'
                             'und Parlament der Schweizerischen Eidgenossenschaft in der Bundesstadt Bern bezeichnet.'
                             'Das Bundeshaus ist ein unter Denkmalschutz stehender symmetrischer Gebäudekomplex'
                             'von etwas mehr als 300 Metern Länge '
              }


def add_doc(coll):
    DiscoBern.Denkmal.insert_one(coll)
    print('Document added:', coll)


def find_coll(key, value):
    for i in DiscoBern.Denkmal.find({key: value}):
        #print(i)
        return i
    return 'not found!!'

def show_all():
    for i in DiscoBern.Denkmal.find():
            print(i)
    return DiscoBern.Denkmal.find()

def find_by(id):
    result = DiscoBern.Denkmal.find_one(ObjectId(id))
    return result


mongo = Blueprint(__name__, "mongo")

@mongo.route('/')
def home():
    results = DiscoBern.Denkmal.find()
    print(type(results))    
    return render_template('mongo.html', sights = results)

@mongo.route('/detail/<id>')
def detail(id):
    result = DiscoBern.Denkmal.find_one(ObjectId(id))
    return render_template('mongo_detail.html', sight = result)


@mongo.route('/delete/<id>')
def delete(id):
    DiscoBern.Denkmal.delete_one(DiscoBern.Denkmal.find_one(ObjectId(id)))
    return redirect('/mongo/')
