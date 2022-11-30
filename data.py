from pymongo import MongoClient

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
    return i



#find_coll('name','Bundeshaus')


'''
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
'''