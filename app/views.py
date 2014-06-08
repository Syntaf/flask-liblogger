from flask import render_template
from app import app

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
