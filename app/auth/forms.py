from flask_wtf import FlaskForm
from ..models import User
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp,EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me Logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, Numbers, dots or '
                                                          'Underscores')])
    password = PasswordField('Password', validators=[InputRequired(), Length(4, 16),
                                                     EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in Use')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[InputRequired()])
    password = PasswordField('New password', validators=[InputRequired(), EqualTo('password2',
                                                                                  message='Passwords must match')])
    password2 = PasswordField('Confirm New Password', validators=[InputRequired()])
    submit = SubmitField('submit')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('Enter New Password', validators=[InputRequired(),
                                                               EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm Password', validators=[InputRequired()])
    submit = SubmitField('Reset Password')
