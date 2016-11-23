#default config
import os
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "\xe2\x9c\xee\xc4%\x8ffS\x95\xa3\xee\xd4\xf4\xed|S\xccN![u\xa2;\x15"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	#'sqlite:///posts.db'
	#'postgresql://postgres:abc123@localhost/posts'
	SOCIAL_TWITTER = {
    'consumer_key': 'twitter consumer key',
    'consumer_secret': 'twitter consumer secret'}

	SOCIAL_FACEBOOK = {
    'consumer_key': '1608967339412134',
    'consumer_secret': '379fe87f981c4d85f72cdb605d157478'}

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False