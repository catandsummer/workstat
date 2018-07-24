# -*- coding: utf-8 -*-
import pymongo

from urllib.parse import quote

from cfg import *


def get_mongo_db(dbname):
	url = "mongodb://%s:%s@%s:%s" % (quote(DB_USERNAME), quote(DB_PASS), DB_IP, DB_PORT)
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
	return [{"data": d["data"], "id":str(d["_id"])} for d in col.find(name=username)]


def del_data(index):
	from bson.objectid import ObjectId
	col = _getcollect()
	try:
		col.remove({"_id": ObjectId(index)})
		return "ok"
	except Exception as e:
		return repr(e)

if __name__ == '__main__':
	db = get_mongo_db('aluba_stat')
	rawdata = db["raw_data"]

	for doc in rawdata.find():
		print(doc)