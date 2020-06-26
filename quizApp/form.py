from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, BooleanField
from wtforms.validators import DataRequired, Length, InputRequired

class RegisterName(FlaskForm):
    userName = StringField('Enter Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Create Quiz')

class SubmitOwn(FlaskForm):
    submitOwn = SubmitField('Create your own questions')

class SubmitReady(FlaskForm):
    submitReady = SubmitField('Ready-made questions')

class ReadymadeForm(FlaskForm):
    submit = SubmitField('SUBMIT')
    skip = SubmitField('SKIP')
    done = SubmitField('DONE')

class OwnMade(FlaskForm):
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    answer = RadioField('option', choices=[(1, 'OPTION NO 1'), (2, 'OPTION NO 2'), (3, 'OPTION NO 3'), (4, 'OPTION NO 4')], default=None, coerce=int, validators=[InputRequired()])
    nxt = SubmitField('NEXT')
    done = SubmitField('DONE')

class PlayQuiz(FlaskForm):
    nxt = SubmitField('SUBMIT')

class PlayerForm(FlaskForm):
    playerName = StringField('Enter Your Name', validators=[DataRequired(), Length(min=2, max=10)])
    play = SubmitField('PLAY')