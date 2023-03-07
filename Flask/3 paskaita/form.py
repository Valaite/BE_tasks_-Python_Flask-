from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class PersonForm(FlaskForm):
    name = StringField('Vardas', validators=[DataRequired(message='Įveskite vardą')])
    l_name = StringField('Pavardė', validators=[DataRequired(message='Įveskite pavardę')])
    comment = TextAreaField('Komentaras', [Optional(), Length(max=200)])
    submit = SubmitField('Pasirašyti')