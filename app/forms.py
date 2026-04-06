from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import Length, DataRequired, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username =StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email =StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password= PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose a different one.')    

class LoginForm(FlaskForm):
    email =StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password= PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    remember =BooleanField('Remember Me')
    submit = SubmitField('Login')



