# -*- coding: utf-8 -*-
import pymongo
try:
    from urllib.parse import quote
except:
    from urllib import quote


def get_mongo_db(dbname):
    url = "mongodb://%s:%s@%s:%s" % (quote("admin"), quote("admin"), "192.168.1.105", "27017")
    return pymongo.MongoClient(url)[dbname]

def _getcollect():
    db = get_mongo_db('workstat_test')
    return db["raw_data"]


def signin(username, passkey):
    db = get_mongo_db('workstat_test')
    col = db["auth"]
    data = col.find_one(name=username)
    if data:
        if data["pass"] == passkey:
            return True
        else:
            return False
    else:
        # signup
        col.insert({"name": username, "pass":passkey})
        return True


def save_data(username, data):
    col = _getcollect()
    col.insert({"name": username, "data": data})

def get_data(username):
    col = _getcollect()
    return list(col.find(name=username))

if __name__ == '__main__':
    db = get_mongo_db('aluba_stat')
    rawdata = db["raw_data"]

    for doc in rawdata.find():
        print(doc)