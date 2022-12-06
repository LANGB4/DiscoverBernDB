from flask import Flask
from mongodb import mongo
from api import api

app = Flask(__name__)
app.register_blueprint(mongo, url_prefix='/mongo')
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, port=8000)