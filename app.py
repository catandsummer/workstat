# -*- coding:utf-8 -*-
from flask import jsonify, render_template
from flask_login import login_required
from flask_base import app
from user import auth


# ==================================
# 下面路由至页面
# ==================================

@app.route('/')
@login_required
def index():
    return render_template('index.html')

def main():
    app.register_blueprint(auth, url_prefix='/auth')
    app.run(debug=True, host='localhost')

if __name__ == '__main__':
    main()
