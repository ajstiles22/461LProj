import random
from flask import Flask, request as req, render_template, json
from flask_cors import CORS, cross_origin
from flask.helpers import send_from_directory
import pymongo
import encryption
import ssl
from pymongo import MongoClient
import ssl

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
cors = CORS(app)


@app.route("/api", methods=['GET'])
@cross_origin()
def index():
    return {
        'name': ['Youngjae, Hur']
    }

# @app.route("/")
# @cross_origin()
# def hello_world():
#     return "<p>Hello, World!</p>"


@app.route("/create", methods=['GET', 'POST'])
@cross_origin()
def create(): 
    client = pymongo.MongoClient("mongodb+srv://koushikck7:Letsgolakers2020!!@cluster0.xg4uw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
    db = client.userset
    setData = db.set
    data = req.json
    username = data['username']
    password = data['password']
    n = 3
    d = -1
    encryptID = encryption.customEncrypt(username, n, d)
    encryptPass = encryption.customEncrypt(password, n, d)
    insertdata = {
        "username": encryptID,
        "password": encryptPass
    }
    setData.insert_one(insertdata)
    check = {'created': "successfully"}
    return check


@app.route("/authenticate", methods=['GET', 'POST'])
@cross_origin()
def authenticate(): 
    client = pymongo.MongoClient("mongodb+srv://koushikck7:Letsgolakers2020!!@cluster0.xg4uw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
    db = client.userset
    setData = db.set
    data = req.json
    username = data['username']
    password = data['password']
    n = 3
    d = -1
    encryptID = encryption.customEncrypt(username, n, d)
    encryptPass = encryption.customEncrypt(password, n, d)
    #res = setData.find({"username": encryptID, "password": encryptPass})
    res = setData.find()
    for r in res:
        if r['username'] == encryptID and r['password'] == encryptPass:
            check = {'authentication': "successful"}
            return check
    check = {'authentication': "failed"}
    return check


@app.route("/hardwareset", methods=["GET", "POST"])
@cross_origin
def hardwareSet():
    client = pymongo.MongoClient("mongodb+srv://koushikck7:Letsgolakers2020!!@cluster0.xg4uw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
    db = client.HWset1
    setData = db.set
    for c in setData.find():
        capacityHW1 = c.capacity
        availabilityHW1 = c.availability

    db = client.HWset2
    setData = db.set
    for c in setData.find():
        capacityHW2 = c.capacity
        availabilityHW2 = c.availability
    


@app.route("/")
@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()
