from app import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class BlogPost(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	description = db.Column(db.String)
	author_id = db.Column(db.Integer, ForeignKey('ngo.id'))

	def __init__(self, title, description):
		self.title = title
		self.description = description

	def __repr__(self):
		return 	"title :{}".format(self.title)


class NGO(db.Model):
	__tablename__ = "ngo"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	description = db.Column(db.String, nullable=False)

	password = db.Column(db.String, nullable=False)
	posts = relationship("BlogPost", backref="author")

	def __init__(self, name, password):
		self.name = name
		self.password = password

	def __repr__(self):
		return '<name {}'.format(self.name)