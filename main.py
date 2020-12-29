from flask import Flask, jsonify, request as req, render_template
import pandas as pd
from sqlalchemy import *
import json

engine = create_engine('mysql+pymysql://root:password@localhost/db_books', echo=False)

metadata = MetaData(bind=None)
app = Flask(__name__,static_folder='app/static',template_folder="app/templates")

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    header['Access-Control-Allow-Methods'] = 'OPTIONS, HEAD, GET, POST, DELETE, PUT'
    return response

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/signIn")
def register():
    return render_template("register.html")