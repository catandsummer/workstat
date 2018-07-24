# -*- coding:utf-8 -*-
from flask import jsonify, render_template, request, session
from flask_login import login_required
from flask_base import app
from user import auth
from Database import save_data, get_data

# ==================================
# 下面路由至页面
# ==================================


@app.route('/')
@login_required
def index():
    return render_template('index.html')


def makelist(datalist):
    ret = ""
    for data in datalist:
        ret+= "<li>%s</li>\n" % data
    return ret

@app.route("/summitdata", methods=['POST'])
@login_required
def summitdata():
    data = request.form.to_dict()
    content = data['content']
    username = session.get('user_id')
    save_data(username, content)
    alldata = get_data(username)
    return render_template('index.html', content=makelist(alldata))


def main():
    app.register_blueprint(auth, url_prefix='/auth')
    app.run(debug=True, host='localhost')

if __name__ == '__main__':
    main()
