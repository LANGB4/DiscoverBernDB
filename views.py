from flask import Blueprint, render_template, jsonify, request
from mongo import Bundeshaus, Kindlifresserbrunnen, show_all, find_coll, find_by, JSONEncoder


views = Blueprint(__name__, "views")

# Examples form Tech with Tim
@views.route('/')
def home():
    return render_template('index.html', info = 'Welcome to the home page!')


@views.route('/profile/<sightname>')
def profile(sightname):
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
        return render_template('index.html', 
                                info = result['Description'],
                                name = result['name'], 
                                id= result['_id'])
    except:
        return render_template('index.html', 
                                info = 'Nothing found, check spelling')


@views.route('/detail/<_id>')
def detail(_id):
    try:
        result = find_by(_id)
        return render_template('index.html', 
                                info = result['Description'],
                                name = result['name'], 
                                id= result['_id'])
    except:
        return render_template('index.html', 
                                info = 'Nothing found, wrong QR-Code')





#trying to return json, loop to create dict?

@views.route('/test')
def test():
    result = find_by('63724a6e57eb8a49e0214769')
    print('test-log:', type(result))
    result2 = JSONEncoder().encode(result)
    result3 = [result2]
    print('test-log2:', type(result2))
    return jsonify(result3)

