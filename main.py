
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

DiscoBern = client.DiscoBern

Denkmal = DiscoBern.Denkmal

Kindlifresserbrunnen = {'name': 'Kindlifresserbrunnen',
                        'address': "Kornhausplatz 18",
                        'buss top': 'Zytglogge',
                        'Description': """Die Brunnenfigur ist eine auf ein Postament 
                                       lehnende Kinderschreckfigur (Kinderfresser, im Englischen Oger),
                                       die gerade ein nacktes Kind verschlingt. In einem umgehängten
                                       Sack befinden sich weitere Kinder. Der Kinderfresser trägt einen spitzen 
                                       Hut mit eingerollter Krempe."""
                        }

Rosengarten = {'name': 'Rosengarten',
               'address': "Alter Argauerstalden 31B",
               'buss top': 'Rosengarten',
               'Description': '''Der Rosengarten gehört zu den schönsten Parks 
                              der Stadt Bern und bietet einen einmaligen Blick 
                              auf die Dachlandschaft der historischen Altstadt, 
                              das Münster und die Aareschlaufe. '''
               }



# DiscoBern.Denkmal.insert_one(Rosengarten)
# DiscoBern.Denkmal.insert_one(Kindlifresserbrunnen)


for i in DiscoBern.Denkmal.find({'name' : 'Kindlifresserbrunnen'}):
    print(i)


for i in DiscoBern.Denkmal.find({'name' : 'Rosengarten'}):
    print(i)


def addDoc(name):
    print('addDoc called with name:', name)


addDoc('Hans')

