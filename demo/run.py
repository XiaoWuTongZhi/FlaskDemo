#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import json
import pymongo

from bson.json_util import dumps
from bson.json_util import loads

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app = Flask(__name__)

@app.route('/home',methods=['GET'])
def home():

    mongo = pymongo.MongoClient(host='mongodb://127.0.0.1', port=27017)
    print ("mongoDB connect status info:",mongo.server_info())

    db = mongo.test

    if 'titles' in db.list_collection_names():
        cursor = db.titles.find({},{'_id':0,'title':1})
        json = loads(dumps(cursor))
        print(json)
        return {'data':json}

    return None


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)