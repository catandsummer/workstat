from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost:3306/todobase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
