from flask import Blueprint, render_template, jsonify, request
from data import Bundeshaus, Kindlifresserbrunnen, show_all, find_coll


views = Blueprint(__name__, "views")

# Examples form Tech with Tim
@views.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the home page!')


@views.route('/detail/<sightname>')
def detail(sightname):
    return render_template('index.html', info = 'here you see the detailed view of ' + sightname)


@views.route('/find')
def find():
    args = request.args
    name = args.get('name')
    # querry: /find?name=XYZ
    return render_template('index.html', info = 'Result: ' + name)


@views.route('/json')
def get_json():
    return jsonify(Kindlifresserbrunnen)



# Code here:


@views.route('/test')
def test():
    result = find_coll('name','Kindlifresserbrunnen')
    return render_template('index.html',  name = result, info = show_all()  )



#TO DO:

#show list of all entries

#show detail of one by qr-code (id) in URL

#add one

# change one

# search by name:

@views.route('/search')
def search():
    args = request.args
    name = args.get('name')
    try:
        result = find_coll('name', name)
        # querry: /find?name=XYZ
        return render_template('index.html', info = 'Result: ' + result['Description'])
    except:
        return render_template('index.html', info = 'Nothing found, check spelling')


