
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

myDB = client.DiscoBern

myColl = myDB['Denkmal']






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

Denkmäler = {
    'Kindlifresserbrunnen': Kindlifresserbrunnen,
    'Rosengarten' : Rosengarten
}

#rec = myDB.myColl.Denkmal.insert_one(Kindlifresserbrunnen)


for i in myDB.myColl.Denkmal.find({'name' : 'Kindlifresserbrunnen'}):
    print(i)


for i in myDB.myColl.Denkmal.find({'name' : 'Rosengarten'}):
    print(i)


"""
if 'address' in Kindlifresserbrunnen:
    print('address:', Kindlifresserbrunnen['address'])
else:
    print('address not found!')
Kindlifresserbrunnen.pop('address')
if 'address' in Kindlifresserbrunnen:
    print('address:', Kindlifresserbrunnen['address'])
else:
    print('address not found!')
for i in Kindlifresserbrunnen:
    print(i, ': ', Kindlifresserbrunnen[i])
for denkmal in Denkmäler:
    print(denkmal, ': ', Denkmäler[denkmal])
"""
