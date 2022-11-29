from flask import Blueprint, render_template, jsonify
from data import Bundeshaus, Kindlifresserbrunnen, show_all, find_coll




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
    result = find_coll('name','Kindlifresserbrunnen')
    return render_template('index.html',  name = result, info = show_all()  )
