# -*- coding:utf-8 -*-
from flask import jsonify, render_template
from flask_login import login_required
from flask_restful import Api
from flask_base import app
from task_mgr import Task
from user import auth
from conf import initialize as init



# ==================================
# 下面路由至页面
# ==================================

@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/__webpack_hmr', methods=['GET'])
def getgmr():
    return jsonify({'result': True}),200


# 定制404出错页面
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


def main():
    init()
    api = Api(app)


    # ==================================
    # 下面是RESTful api 注册
    # ==================================

    api.add_resource(Task, '/todoapi/tasks/')

    app.register_blueprint(auth, url_prefix='/auth')
    app.run(debug=True, host='localhost')

if __name__ == '__main__':
    main()
