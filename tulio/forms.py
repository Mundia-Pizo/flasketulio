from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, SubmitField, PasswordField,TextAreaField
from wtforms.validators import DataRequired,EqualTo, Length, Email,  ValidationError
from flask_bcrypt import Bcrypt
from tulio.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed



class RegistrationForm(FlaskForm):
	username=StringField('Username', validators=[
		      DataRequired(),Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('Comform Password',
	                 validators=[DataRequired(), EqualTo('password')] )
	submit=SubmitField('Sign up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already exists use another')


	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('User with this email already exists use another')

class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(), Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username=StringField('Username', validators=[
		      DataRequired(),Length(min=2, max=20)])
	email=StringField('Email',validators=[DataRequired(), Email()])
	picture=FileField('Update profile picture'\
		 ,validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
	submit=SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username already exists user another')


	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('User with this email already exists user another')


class PostForm(FlaskForm):
	title=StringField('Title', validators=[DataRequired()])
	content=TextAreaField('Content', validators=[DataRequired()])
	submit=SubmitField('Post')

class ProductForm(FlaskForm):
	title=StringField('Title', validators=[DataRequired()])
	product_description=TextAreaField('Details', validators=[DataRequired()])
	product_picture=FileField('Upload product image'\
            ,validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
	submit=SubmitField('Add Product')

