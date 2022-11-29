from flask import Blueprint, render_template, jsonify
from data import Bundeshaus, Kindlifresserbrunnen
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

DiscoBern = client.DiscoBern



views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the home page!'  )

@views.route('/detail/<sightname>')
def detail(sightname):
    return render_template('index.html', info = 'here you see the detailed view of ' + sightname)


@views.route('/json')
def get_json():
    return jsonify(Kindlifresserbrunnen)

@views.route('/test')
def test():
    for i in DiscoBern.Denkmal.find({'name':'Kindlifresserbrunnen'}):
            print('id: ', i['_id'], 'name:', i['name'])
    return render_template('index.html', id = i['_id'], name = i['name'], info = 'This is the test page'  )
