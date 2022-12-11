from pymongo import MongoClient
from bson import ObjectId
from flask import Blueprint, render_template, request, redirect


client = MongoClient('localhost', 27017)
DiscoBern = client.DiscoBern


mongo = Blueprint(__name__, "mongo")


@mongo.route('/')
def home():
    results = DiscoBern.Denkmal.find()
    return render_template('/mongo/index.html', sights = results)


@mongo.route('/detail/<id>')
def detail(id):
    result = DiscoBern.Denkmal.find_one(ObjectId(id))
    return render_template('mongo/detail.html', sight = result)


@mongo.route('/delete/<id>')
def delete(id):
    DiscoBern.Denkmal.delete_one(DiscoBern.Denkmal.find_one(ObjectId(id)))
    return redirect('/mongo/')


@mongo.route('/put', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        try:
            DiscoBern.Denkmal.insert_one({'name': request.form['name'],
                                        'text': request.form['text'],
                                        'long': request.form['long'],
                                        'lat': request.form['lat'],
                                        'comment': request.form['comment']})
            return redirect('/mongo/')
        except:
            return render_template('Error.html', message = 'something went wrong posting your sight..')
    else:
        return redirect('/mongo/')    


@mongo.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    result = DiscoBern.Denkmal.find_one(ObjectId(id))
    if request.method == 'POST':
        try:
            DiscoBern.Denkmal.update_one(DiscoBern.Denkmal.find_one(ObjectId(id)),
                                        {"$set": 
                                        {'name': request.form['name'],
                                        'text': request.form['text'],
                                        'long': request.form['long'],
                                        'lat': request.form['lat'],
                                        'comment': request.form['comment']}})
            return redirect('/mongo/detail/' + id)
        except:
            return render_template('Error.html', messsage = 'mongo update failed')
    else:
        return render_template('mongo/update.html', sight = result)
        
    