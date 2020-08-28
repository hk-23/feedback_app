import os
import json
from flask import Flask, request, render_template, redirect, url_for,jsonify,make_response,abort,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY','justanormalsecretkeywithnomeaning')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80),unique=True,nullable=False)
	password = db.Column(db.String(80),nullable=False)

db.create_all()

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def sigup():
	if request.method == "POST":
		username = request.form.get('username')
		password = request.form.get('password')
		user = User(username=username,password=password)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('signup.html')

@app.route('/signup/vue',methods=['POST','GET'])
def vue_signup():
	if request.method=="POST":
		username = request.form.get('username',0)
		password = request.form.get('password',0)
		if username and password:
			if User.query.filter_by(username=username).first():
				abort(404,description='username already exist')
			user = User(username=username,password=password)
			db.session.add(user)
			db.session.commit()
			flash('Signed In successfully')
			return redirect(url_for('home'))
		else:
			abort(404,description='username or password not found')
	return render_template('signup-vue.html',context=None)

@app.route('/signup/username/check',methods=["POST"])
def username_check():
	if request.form.get('username',0):
		print(User.query.filter_by(username=request.form.get('username')).first())
		if User.query.filter_by(username=request.form.get('username')).first():
			print('True')
			return jsonify({'available':False})
		else:
			print('false')
			return jsonify({'available':True})
	else:
		print('error')
		return make_response(400)

@app.route('/login/<path:next>')
def login():
	pass

@app.route('/logout')
def logout():
	pass

@app.route('/admin')
def admin():
	l = User.query.filter().all()
	context = {
		'user_data': l,
	}
	return render_template('admin.html',context=context)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html',e=e), 404

if __name__ == '__main__':
	app.run(debug=True)