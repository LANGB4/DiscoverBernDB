from flask import Blueprint, render_template, jsonify, request
from mongodb import Bundeshaus, Kindlifresserbrunnen, show_all, find_coll, find_by, JSONEncoder


mongo = Blueprint(__name__, "mongo")

# Examples form Tech with Tim
@mongo.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the home page!')



