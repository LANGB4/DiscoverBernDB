from pymongo import MongoClient

client = MongoClient('localhost', 27017)

DiscoBern = client.DiscoBern

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


def addDoc(coll):
    DiscoBern.Denkmal.insert_one(coll)
    print('Document added:', coll)

def findColl(key, value):
    for i in DiscoBern.Denkmal.find({key: value}):
        return i
    print(key, ':', value, 'not found!!')
    return {}



result = findColl('buss top', 'Zytglogge')
print(result['_id'])

#for i in result:
 #   print(i, ':', result[i])

    

class Denkmal:
    def __init__(self, id, name, desc, lati, long):
        self.id = id
        self.name = name
        self.description = desc
        self.latitide = lati
        self.longitude = long


Bp = Denkmal(0.1,'test','das ist die kurzbeschreibung',41.8755616,-87.6244212)


while True:
    inp = int(input('*** press 0 and then enter to exit ***\n'
                    '*** press 1 to list all Denkmäler-id present in DB *** \n'
                    '*** press 2 to add new Denkmal ***\n'))

    if inp == 0:
        print('closing program, adios')
        break

    elif inp == 1:
        for i in DiscoBern.Denkmal.find():
            print('id: ', i['_id'], 'name:', i['name'])

    elif inp == 2:
        name = str(input('*** type the name of the denkmal here: \n'))
        print(name, 'is noted')

