from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Pitch yourself, aka bio', validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    pitch_comment=TextAreaField('Comment on this pitch', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    pitch_category = StringField('Enter the category', validators=[Required()])
    pitch_body=TextAreaField('Enter your pitch')
    submit=SubmitField('Submit')
