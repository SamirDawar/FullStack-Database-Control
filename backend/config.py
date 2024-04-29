#file configuration
#building API in flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  #allows us to send requests to this backend from other URLS

app = Flask(__name__)
CORS(app) #disables CORS error

#specifying location of the database is our local machine
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  #dont track all modifications made to the database


#creates database instance which gives us access to the database we just created
db = SQLAlchemy(app)