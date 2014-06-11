#!flask/bin/python
import os
import unittest
from datetime import datetime, timedelta

from config import basedir
from app import app, db
from app.models import User, Post

class TestCase(unittest.TestCase):
	def test_follow_posts(self):
		u1 = User(nickname = 'jim', email='something@example.com')
		u2 = User(nickname = 'susan', email='susan@example.com')
		u3 = User(nickname = 'bob', email='bob@example.com')
		u4 = User(nickname = 'Grant', email='grant@grant.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.add(u3)
		db.session.add(u4)
		#create posts
		utcnow = datetime.utcnow()
		p1 = Post(body="post from jim", author=u1,timestamp=utcnow+timedelta(seconds=1))
		p2 = Post(body="post from susan", author=u2,timestamp=utcnow+timedelta(seconds=2))
		p3 = Post(body="post from bob", author=u3,timestamp=utcnow+timedelta(seconds=3))
		p4 = Post(body="post from grant", author=u4,timestamp=utcnow+timedelta(seconds=4))
		db.session.add(p1)
		db.session.add(p2)
		db.session.add(p3)
		db.session.add(p4)
		db.session.commit()
		#set up followers
		u1.follow(u1) #jim follows himself
		u1.follow(u2) #jim follows susan
		u1.follow(u4) #jim follows grant
		u2.follow(u2) #susan follows herself
		u2.follow(u3) #susan follows bob
		u3.follow(u3) #bob follows himself
		u3.follow(u4) #bob follows grant
		u4.follow(u4) #grant follows himself
		db.session.add(u1)
		db.session.add(u2)
		db.session.add(u3)
		db.session.add(u4)
		db.session.commit()
		#check the followed posts of each user
		f1 = u1.followed_posts().all()
		f2 = u2.followed_posts().all()
		f3 = u3.followed_posts().all()
		f4 = u4.followed_posts().all()
		assert len(f1)==3
		assert len(f2)==2
		assert len(f3)==2
		assert len(f4)==1
		assert f1 == [p4,p2,p1]
		assert f2 == [p3,p2]
		assert f3 == [p4,p3]
		assert f4 == [p4]
	def test_follow(self):
		u1 = User(nickname = 'john', email = 'john@example.com')
		u2 = User(nickname = 'susan', email = 'sustan@example.com')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		assert u1.unfollow(u2) == None
		u = u1.follow(u2)
		db.session.add(u)
		db.session.commit()
		assert u1.follow(u2) == None
		assert u1.is_following(u2)
		assert u1.followed.count() == 1
		assert u1.followed.first().nickname == 'susan'
		assert u2.followers.count() == 1
		assert u2.followers.first().nickname == 'john'
		u = u1.unfollow(u2)
		db.session.add(u)
		db.session.commit()
		assert u1.is_following(u2) == False
		assert u1.followed.count() == 0
		assert u1.followers.count() == 0

	def setUp(self):
		app.config['TESTING'] = True
		app.config['CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
		self.app = app.test_client()
		db.create_all()
	
	def tearDown(self):
		db.session.remove()
		db.drop_all()

	def test_avatar(self):
		u = User(nickname = 'john', email = 'john@example.com')
		avatar = u.avatar(128)
		expected = 'http://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6'
		assert avatar[0:len(expected)] == expected
	
	def test_make_unique_nickname(self):
		u = User(nickname = 'john', email = 'john@example.com')
		db.session.add(u)
		db.session.commit()
		nickname = User.make_unique_nickname('john')
		assert nickname != 'john'
		u = User(nickname = nickname, email = 'susan@example.com')
		db.session.add(u)
		db.session.commit()
		nickname2 = User.make_unique_nickname('john')
		assert nickname2 != 'john'
		assert nickname2 != nickname

if __name__ == '__main__':
	unittest.main()
