# -*- coding: utf-8 -*-
import pymongo
try:
    from urllib.parse import quote
except:
    from urllib import quote


def get_mongo_db(dbname):
    url = "mongodb://%s:%s@%s:%s" % (quote("admin"), quote("admin"), "192.168.1.105", "27017")
    return pymongo.MongoClient(url)[dbname]

if __name__ == '__main__':
    db = get_mongo_db('aluba_stat')
    rawdata = db["raw_data"]
    for doc in rawdata.find():
        print(doc)