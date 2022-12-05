from flask import Blueprint, render_template, redirect, abort, url_for, request
import requests


api = Blueprint(__name__, "api")
BASE = 'http://127.0.0.1:5000/'




@api.route('/')
def home():
    response = requests.get(BASE + 'sight/all')
    #print(response.json())
    if 'message' in response.json():
        print('message in response.json')
        return render_template('index.html', sights = 'no_data')
    else:
        return render_template('index.html', sights = response.json())


@api.route('/detail/<sight_id>')
def get_json(sight_id):
    response = requests.get(BASE + 'sight/' + sight_id)
    
    return render_template('detail.html', 
                            id = sight_id,
                            info = response.json()['text'],
                            name = response.json()['name'],
                            zip = response.json()['zip'],)

@api.route('/delete/<sight_id>')
def delete(sight_id):
    response = requests.delete(BASE + 'sight/' + sight_id)
    print(response)
    return redirect('/api/')

@api.route('/put', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        sight_id = request.form['id']
        sight_name = request.form['name']
        sight_text = request.form['text']
        sight_zip = request.form['zip']
        try:
            response = requests.put(BASE + 'sight/' + sight_id, {'name': sight_name, 'text': sight_text, 'zip': sight_zip})
            print(response.json())
            return redirect('/api/')
        except:
            return render_template('index.html', sights = 'something went wrong..')
    else:
        redirect('/api/')

    


    
    ''''''





