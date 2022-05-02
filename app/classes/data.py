# This is where all the database collections are defined. A collection is a place to hold a defined 
# set of data like Users, Posts, Comments. Collections are defined below as classes. Each class name is 
# the name of the data collection and each item is a data 'field' that stores a piece of data.  Data 
# fields have types like IntField, StringField etc.  This uses the Mongoengine Python Library. When 
# you interact with the data you are creating an onject that is an instance of the class.

from pandas import BooleanDtype
from app import app
from flask import flash
from flask_login import UserMixin
from mongoengine import FileField, EmailField, StringField, ReferenceField, DateTimeField, CASCADE, BooleanField
from flask_mongoengine import Document
from werkzeug.security import generate_password_hash, check_password_hash
import datetime as dt
import jwt
from time import time

#from bson.objectid import ObjectId

class User(UserMixin, Document):
    username = StringField()
    password_hash = StringField()
    fname = StringField()
    lname = StringField()
    email = EmailField()
    image = FileField()
    role = StringField()
    agerange = StringField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        id=str(self.id)
        return jwt.encode({'reset_password': id, 'exp': time() + expires_in},app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            flash("Could not verify reset password token.")
            return
        return User.objects.get(pk=id)

class Post(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    posttype = StringField()
    content = StringField()
    createdate = DateTimeField(default=dt.datetime.utcnow)
    modifydate = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Comment(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    post = ReferenceField('Post',reverse_delete_rule=CASCADE)
    # This could be used to allow comments on comments
    # comment = ReferenceField('Comment',reverse_delete_rule=CASCADE)
    content = StringField()
    createdate = DateTimeField(default=dt.datetime.utcnow)
    modifydate = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class HomeDef(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE) 
    subject = StringField()
    definition = StringField()
    homeimg = FileField()
    createdate = DateTimeField(default=dt.datetime.utcnow)
    modifydate = DateTimeField()

    meta = {
        'ordering': ['-createdate']
    }

class Challenge(Document):
    author = ReferenceField('User',reverse_delete_rule=CASCADE)
    challenge1 = BooleanField('whatever challenge 1 is')
    challenge2 = BooleanField('whatever challenge 2 is')
    challenge3 = BooleanField('whatever challenge 3 is')
    challenge4 = BooleanField('whatever challenge 4 is')
    challenge5 = BooleanField('whatever challenge 5 is')
    challenge6 = BooleanField('whatever challenge 6 is')
    challenge7 = BooleanField('whatever challenge 7 is')
    challenge8 = BooleanField('whatever challenge 8 is')
    challenge9 = BooleanField('whatever challenge 9 is')
    challenge10 = BooleanField('whatever challenge 10 is')
    reflection1 = StringField()
    reflection2 = StringField()
    reflection3 = StringField()
    reflection4 = StringField()
    reflection5 = StringField()
    reflection6 = StringField()
    reflection7 = StringField()
    reflection8 = StringField()
    reflection9 = StringField()
    reflection10 = StringField()

