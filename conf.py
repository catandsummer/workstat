# -*- coding:utf-8 -*-
import json
USER_CONF_PATH = 'static/data/user_conf.json'

user_conf = {}

print 'init'


def saveconf():
    with open(USER_CONF_PATH, 'w') as json_file:
        json_file.write(json.dumps(user_conf))


def initialize():
    import os
    global user_conf
    try:
        if os.path.exists(USER_CONF_PATH):
            with open(USER_CONF_PATH) as json_file:
                user_conf = json.load(json_file)
        else:
            user_conf = {'idcount':1000,'taskcount':100000}
            with open(USER_CONF_PATH, 'w') as json_file:
                json_file.write(json.dumps(user_conf))
        print user_conf
    except Exception as e:
        print e