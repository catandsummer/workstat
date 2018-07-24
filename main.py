# -*- coding:utf-8 -*-
from flask import jsonify, render_template, request, session, redirect
from flask_login import login_required

from user import auth
from Database import save_data, get_data, del_data
from app import app


@app.route('/')
@login_required
def index():
	return render_template('index.html')


@app.route("/datainterface", methods=['POST', "GET", "DEL"])
@login_required
def datainterface():
	username = session.get('user_id')
	data = request.form.to_dict()
	if request.method == "POST":

		content = data['content']

		save_data(username, content)
		return redirect("/")
	elif request.method == "GET":
		return jsonify({"data": get_data(username)})
	elif request.method == "DEL":
		_id = data['index']
		del_data(_id)
		return "ok"


def main():
	app.register_blueprint(auth, url_prefix='/auth')
	app.run(debug=True, host='localhost')


if __name__ == '__main__':
	main()
