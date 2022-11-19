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

Bundeshaus = {'name': 'Bundeshaus',
              'address': "Bundesplatz 3",
              'buss top': 'Bundesplatz',
              'Description': '''Als Bundeshaus wird der Sitz von Regierung 
               und Parlament der Schweizerischen Eidgenossenschaft in der Bundesstadt Bern bezeichnet. 
               Das Bundeshaus ist ein unter Denkmalschutz stehender symmetrischer Gebäudekomplex 
               von etwas mehr als 300 Metern Länge'''
              }


def addDoc(coll):
    DiscoBern.Denkmal.insert_one(coll)
    print('Document added:', coll)

def findColl(key, value):
    for i in DiscoBern.Denkmal.find({key: value}):
        return i
    print(key, ':', value, 'not found!!')
    return {}

#addDoc(Bundeshaus)

result = findColl('buss top', 'Zytglogge')
print(result)
for i in result:
    print(i, ':', result[i])

    
