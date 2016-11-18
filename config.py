#default config
import os
class BaseConfig(object):
	DEBUG = False
	SECRET_KEY = "\xe2\x9c\xee\xc4%\x8ffS\x95\xa3\xee\xd4\xf4\xed|S\xccN![u\xa2;\x15"
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
	#'sqlite:///posts.db'

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False