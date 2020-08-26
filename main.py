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

if __name__ == '__main__':
	app.run(debug=True)