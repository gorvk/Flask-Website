from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterName(FlaskForm):
    userName = StringField('Enter Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Create Quiz')

class OwnTypeForm(FlaskForm):
    submitOwn = SubmitField('Create your own questions')

class ReadyTypeForm(FlaskForm):
    submitReady = SubmitField('Ready-made questions')