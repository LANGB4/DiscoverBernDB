from flask import Flask
from views import views
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

DiscoBern = client.DiscoBern

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/views')







if __name__ == '__main__':
    app.run(debug=True)