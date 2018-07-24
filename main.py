# -*- coding:utf-8 -*-
from flask import jsonify, render_template, request, session, redirect
from flask_login import login_required

from user import auth
from Database import save_data, get_data
from app import app


@app.route('/')
@login_required
def index():
	return render_template('index.html')


@app.route("/datainterface", methods=['POST', "GET", "DEL"])
@login_required
def datainterface():
	if request.method == "POST":
		data = request.form.to_dict()
		content = data['content']
		username = session.get('user_id')
		save_data(username, content)
		return redirect("/")
	elif request.method == "GET":
		username = session.get('user_id')
		return jsonify({"data": get_data(username)})
	elif request.method == "DEL":
		return ""


def main():
	app.register_blueprint(auth, url_prefix='/auth')
	app.run(debug=True, host='localhost')


if __name__ == '__main__':
	main()
