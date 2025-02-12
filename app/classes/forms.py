# This file is where data entry forms are created. Forms are placed on templates
# and users fill them out.  Each form is an instance of a class. Forms are managed by the
# Flask-WTForms library.

from flask.app import Flask
from flask import flash
from flask_wtf import FlaskForm
from mongoengine.fields import EmailField
import mongoengine.errors
from wtforms.validators import URL, NumberRange, Email, Optional, InputRequired, ValidationError, DataRequired, EqualTo
from wtforms import PasswordField, StringField, SubmitField, TextAreaField, HiddenField, IntegerField, SelectField, FileField, BooleanField
from app.classes.data import User


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember me')
    submit = SubmitField('submit')


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    fname = StringField('first name', validators=[DataRequired()])
    lname = StringField('last name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('repeat password', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self, username):
        try:
            User.objects.get(username=username.data)
        except mongoengine.errors.DoesNotExist:
            flash(f"{username.data} is available.")
        else:
            raise ValidationError('this username is taken.')

    def validate_email(self, email):
        try:
            User.objects.get(email=email.data)
        except mongoengine.errors.DoesNotExist:
            flash(f'{email.data} is a unique email address.')
        else:
            raise ValidationError(
                'this email address is already in use. if you have forgotten your credentials, you can try to recover your account.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('request password reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField(
        'repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('request password reset')


class ProfileForm(FlaskForm):
    fname = StringField('first name', validators=[DataRequired()])
    lname = StringField('last name', validators=[DataRequired()])
    image = FileField("image")
    submit = SubmitField('submit')
    role = SelectField(
        'role', choices=[("none", "none"), ("admin", "admin"), ("user", "user")])
    agerange = SelectField('age', choices=[("not specified", "not specified"),
                                           ("<12", "<12"), ("12-17", "12-17"), ("18-24", "18-24"), ("25-34", "25-34"), ("35-44", "35-44"), ("45-54", "45-54"), ("55-64", "55-64"), ("65-74", "65-74"), ("75+", "75+")])


class PostForm(FlaskForm):
    subject = StringField('subject', validators=[DataRequired()])
    posttype = SelectField('post type', validators=[DataRequired()], choices=[
                           ("asking a question", "asking a question"), ("sharing", "sharing")])
    content = TextAreaField('post', validators=[DataRequired()])
    submit = SubmitField('post')


class CommentForm(FlaskForm):
    content = TextAreaField('comment', validators=[DataRequired()])
    submit = SubmitField('post')


class HomeDefForm(FlaskForm):
    subject = StringField('subject', validators=[DataRequired()])
    definition = TextAreaField('definition', validators=[DataRequired()])
    homeimg = FileField('image')
    submit = SubmitField('submit')


class ChallengeForm(FlaskForm):
    write1 = BooleanField("what is something you've been struggling with recently?")
    write2 = BooleanField("write about your biggest fear + be honest with yourself.")
    write3 = BooleanField("what is your first memory of life?")
    write4 = BooleanField("what is biggest obstacle you’ve had to overcome?")
    write5 = BooleanField("write about a secret no one knows about you.")
    write6 = BooleanField("what does home mean to you?")
    art1 = BooleanField("create what you fear.")
    art2 = BooleanField("illustrate and ongoing struggle in your life.")
    art3 = BooleanField("create a piece of home.")
    art4 = BooleanField("what does home look like to you?")
    reflection1 = TextAreaField('main ideas from prompt')
    reflection2 = TextAreaField('main ideas from prompt')
    reflection3 = TextAreaField('main ideas from prompt')
    reflection4 = TextAreaField('main ideas from prompt')
    reflection5 = TextAreaField('main ideas from prompt')
    reflection6 = TextAreaField('main ideas from prompt')
    reflection7 = TextAreaField('main ideas from prompt')
    reflection8 = TextAreaField('main ideas from prompt')
    reflection9 = TextAreaField('main ideas from prompt')
    reflection10 = TextAreaField('main ideas from prompt')
    submit = SubmitField('submit')


