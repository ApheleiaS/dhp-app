from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, FloatField, IntegerField
from wtforms.validators import InputRequired,DataRequired, Email, NumberRange

class ParticipantForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email',  [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    age = IntegerField('Age', [NumberRange(min=1, max=150)])
    eyesightr = FloatField('Right Eyesight', [NumberRange(min=-15, max=15)])
    eyesightl = FloatField('Left Eyesight', [NumberRange(min=-15, max=15)])
    gender = SelectField('gender', choices=[('M', 'Male'), ('F', 'Female')])
    profession = SelectField('profession', choices=[('weaver', 'Weaver'), ('artist','Artist'),('student', 'Student'), ('professor', 'Professor'), ('other','Other')])