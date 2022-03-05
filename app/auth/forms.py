from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    username = StringField('Enter your preferred username', validators=[Required()])
    email = StringField("Enter your preferred email address", validators=[Required(), Email()])
    password= PasswordField('Password', validators=[Required(), EqualTo('password_config', message='{asswords must match')])
    password_confirm=PasswordField('Config Password', validators=[Required()])
    submit = SubmitField('Sign UP')