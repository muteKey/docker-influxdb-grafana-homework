#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from datetime import datetime
import logging
import os

app = Flask(__name__)

def elastic():
    es = Elasticsearch(hosts=[{"host":'elasticsearch'}])
    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.now(),
    }
    res = es.index(index="test-index", id=1, document=doc)
    print(res['result'])

    res = es.get(index="test-index", id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", query={"match_all": {}})
    print("Got %d Hits:" % res['hits']['total']['value'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

def mongo():
    try:
        client = MongoClient(os.environ.get('MONGO_URL'))
        client.server_info()
        db = client['test']
        collection = db['TestCollection']
        cursor = collection.find({})
        for document in cursor:
            logging.warning(document)

    except Exception as e:
        print(e)

@app.route('/')
def hello_world():
    mongo()
    elastic()
    return "<p>Hello, World!</p>"
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

