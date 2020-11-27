from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from project.models import User


class LoginForm(FlaskForm):

    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(message='Enter a valid email.')])
    #username = StringField('Username',validators=[DataRequired()])

    # password = PasswordField('password', validators=[DataRequired(), EqualTo(
    #     'confirm_pass', message='Password does not match')])
    password = PasswordField('password', validators=[DataRequired(),Length(min=6, message='Select a stronger password.')])

    #confirm_pass = PasswordField('Confirm Password',validators=[DataRequired()])
    # submit = SubmitField('register')

    # def check_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Your email has been already Registered')

    # def check_username(self, field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username is taken')
