from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="' + form.openid.data + '", remember_me =' + str(form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',
			title = 'Sign In',
			form = form,
			providers = app.config['OPENID_PROVIDERS'])

@app.route('/')
@app.route('/index')
def index():
	user = { 'nickname': 'Grant' } # fake user
	posts = [ # fake array of posts
		{
			'author': { 'nickname': 'John'},
			'body': 'Lovely day in Baton Rouge!'
		},
		{
			'author': { 'nickname': 'Susan'},
			'body': 'Loved the movie!'
		}
	]
	
	return render_template("index.html",
			title = 'Home',
			user = user,
			posts = posts)
