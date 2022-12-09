'''from flask import Blueprint, render_template, jsonify, request
#from mongodb import Bundeshaus, Kindlifresserbrunnen, show_all, find_coll, find_by, JSONEncoder
from pymongo import MongoClient
from bson import ObjectId
from bson.objectid import ObjectId



mongo = Blueprint(__name__, "mongo")


client = MongoClient('localhost', 27017)

DiscoBern =  client.Denkmal




@mongo.route('/')
def home():
    
    #result = find_by('63724a567a4a7a7fb075a310')
    #print(find_by('63724a567a4a7a7fb075a310'))
    #print(result)
    result = DiscoBern.Denkmal.find_one(ObjectId('63724a567a4a7a7fb075a310'))
    return render_template('mongo.html', test = result)


name': request.form['name'],
                                        'text': request.form['text'],
                                        'long': request.form['long'],
                                        'lat': request.form['lat'],
                                        'comment': request.form['comment']


'''


