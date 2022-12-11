from flask import Blueprint, render_template, redirect, request
import requests


api = Blueprint(__name__, "api")
BASE = 'http://127.0.0.1:5000/'


@api.route('/')
def home():
    try:
        response = requests.get(BASE + 'sight/all')
    except:
        return render_template('error.html', message = 'API not reached... ')
    if 'message' in response.json():
        print('message in response.json')
        return render_template('API/index.html', sights = 'no_data')
    else:
        return render_template('API/index.html', sights = response.json())


@api.route('/detail/<sight_id>')
def get_json(sight_id):
    response = requests.get(BASE + 'sight/' + sight_id)
    return render_template('API/detail.html', 
                            id = sight_id,
                            info = response.json()['text'],
                            name = response.json()['name'],
                            zip = response.json()['zip'],)


@api.route('/delete/<sight_id>')
def delete(sight_id):
    requests.delete(BASE + 'sight/' + sight_id)
    return redirect('/api/')


@api.route('/put', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        requests.put(BASE + 'sight/' + request.form['id'],
                    {'name': request.form['name'],
                    'text': request.form['text'],
                    'zip': request.form['zip']})
        return redirect('/api/')
            
    else:
        return redirect('/api/')


@api.route('/update/<sight_id>', methods=['POST', 'GET'])
def update(sight_id):
    response = requests.get(BASE + 'sight/' + sight_id)
    if request.method == 'POST':
        response = requests.patch(BASE + 'sight/' + sight_id,
                                {'name': request.form['name'],
                                'text': request.form['text'],
                                'zip': request.form['zip']})
        return redirect('/api/detail/' + sight_id)
    else: 
        return render_template('API/update.html', sights = response.json())
        
    

    


    





