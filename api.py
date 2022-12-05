from flask import Blueprint, render_template, redirect, abort, url_for
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





