# -*- coding:utf-8 -*-
from flask import request, abort
from flask_restful import Resource
from task_db import Todo, db,db_to_dict
from flask_login import current_user
from user import User

class Task(Resource):
    def post(self):
        '''
        :return:
        '''
        qs = request.args.get('req')
        if qs == 'add':
            if not request.json or not 'description' in request.json:
                abort(400)
            print current_user

            task = Todo(request.json['starttime'], request.json.get('description', ""),current_user.id)

            db.session.add(task)
            db.session.commit()
            return {'task': db_to_dict(task)}, 201

        elif qs == 'check':
            print request.json
            if not request.json or not 'id' in request.json or not 'status' in request.json:
                abort(400)
            task = Todo.query.filter_by(id=request.json['id'],user_id = current_user.id).first()
            if task is None:
                abort(404)
            else:
                print task

            if not request.json['status']:
                task.done = True
            else:
                task.done = False
            tasks = Todo.query.filter_by(user_id=current_user.id).all()
            taskall = list(map(db_to_dict, tasks))
            taskdone = [task for task in taskall if task['done']]
            tasktodo = [task for task in taskall if not task['done']]
            db.session.commit()
            return {'taskdone': taskdone, 'tasktodo': tasktodo}, 201

    def get(self):
        '''
        获取任务列表
        :param taskstr: all：全部任务
        :return:
        '''
        qs=request.args.get('taskstr')
        if not current_user.is_authenticated:
            abort(403)
        print qs
        if qs == "all":

            tasks = Todo.query.filter_by(user_id=current_user.id).all()
            taskall = list(map(db_to_dict, tasks))
            taskdone = [task for task in taskall if task['done']]
            tasktodo = [task for task in taskall if not task['done']]
            return {'taskdone': taskdone, 'tasktodo': tasktodo}
        else:
            pass