from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80),unique=True,nullable=False)
	password = db.Column(db.String(80),nullable=False)

db.create_all()

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup')
def sigup():
	return render_template('signup.html')

@app.route('/login/<path:next>')
def login():
	pass

@app.route('/logout')
def logout():
	pass

if __name__ == '__main__':
	app.run(debug=True)