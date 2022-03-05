from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Pitch yourself, aka bio', validators=[Required()])
    submit = SubmitField('Submit')
