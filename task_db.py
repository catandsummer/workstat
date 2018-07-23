# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
from flask_base import app

import conf
db = SQLAlchemy(app)

def db_to_dict(task):
    return dict(id=task.id,
                starttime=task.starttime,
                description=task.description,
                done=task.done)

# 定义ORM
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starttime = db.Column(db.String(80))
    description = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user_db.id'))
    done = db.Column(db.Boolean)

    def __init__(self, starttime, description, user_id):

        print conf.user_conf
        self.id = conf.user_conf['taskcount']
        conf.user_conf['taskcount'] += 1
        conf.saveconf()
        # TODO 把conf这个做成更新接口，不要直接改
        self.starttime = starttime
        self.description = description
        self.done = False
        self.user_id = user_id

    def __repr__(self):
        return '<Todo %r>' % self.starttime


class User_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    passkey = db.Column(db.String(40))

    def __init__(self, newid, newname, newpass):
        self.id = newid
        self.username = newname
        print (newpass)
        self.passkey = str(newpass)[0:16]

    def __repr__(self):
        return '<User_db %r:%s>' % (self.id, self.username)

# 创建表格、插入数据
@app.before_first_request
def create_db():
    # Recreate database each time for demo
    # db.drop_all()
    # db.create_all()
    pass
    # tasks = [Todo('2017-10-20 12:46:48', u'写代码', False)]
    # db.session.add_all(tasks)
    # db.session.commit()
