from pymongo import MongoClient
from bson.objectid import ObjectId

import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)




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

