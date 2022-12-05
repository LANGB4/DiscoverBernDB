from flask import Blueprint, render_template, jsonify, request
import requests


api = Blueprint(__name__, "api")
BASE = 'http://127.0.0.1:5000/'




@api.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the API page!')


@api.route('/detail/<sight_id>')
def detail(sight_id):
    #response = requests.get(BASE + 'sight/'+sight_id)
    response = requests.get(BASE + 'sight/1')
    print('id:',1,response.json())
    return render_template('index.html', info = response.json())

