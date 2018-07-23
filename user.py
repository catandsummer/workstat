# -*- coding:utf-8 -*-
from flask import jsonify, render_template, Blueprint,request,abort,redirect, url_for, session
from flask_login import (LoginManager, login_required, login_user, logout_user, UserMixin,current_user)
from flask_base import app
from task_db import User_db, db
import hashlib
import conf

_userdb = dict()


# user models
class User(UserMixin):
    def __init__(self, newname, newpass):
        self.name = newname
        self.passkey = newpass

    def get_id(self):
        return self.name



# flask-login
app.secret_key = 'qwpoSDFJsldkfj10'
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    if user_id in _userdb:
        return _userdb[user_id]
    else:
        return None

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def login_show():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login():
    if not request.json or not 'password' in request.json or not 'username' in request.json:
        abort(400)
    username = request.json['username']
    password = request.json['password']
    if username == '' or password == '':
        return jsonify({'result': '用户名不存在'}), 403

    user = _userdb.get(username)
    m = hashlib.md5()
    m.update(password)
    hashpass = m.hexdigest()[0:16]
    print 'hashpass=', hashpass
    print user
    if user == None:
        # 目前自动注册，以后删除
        # TODO
        user = User(username, hashpass)
        _userdb[username] = user
    else:
        if hashpass[0:16] != user.passkey[0:16]:
            logout_user()
            print "密码错误"
            return jsonify({'result': '密码错误'}), 403

    login_user(user)
    next = request.args.get('next')
    return redirect(next or '/')

@app.route('/getname', methods=['GET'])
def getname():
    print(session)
    return jsonify({"user_name": session.get('user_id')}), 200

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'result': 0}), 201
