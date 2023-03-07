from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import app

def lecturer_query():
    return app.Lecturer.query

def get_pk(obj):
    return str(obj)

class StudentForm(FlaskForm):
    name = StringField('Vardas', validators=[DataRequired(message='Įveskite vardą')])
    l_name = StringField('Pavardė', validators=[DataRequired(message='Įveskite pavardę')])
    lessons = QuerySelectMultipleField(query_factory=app.Lesson.query.all, get_label="name", get_pk=get_pk)
    submit = SubmitField('Pridėti studentą')
    
class LessonForm(FlaskForm):
    name = StringField('Pavadinimas', validators=[DataRequired(message='Įveskite pavadinimą')])
    lecturer = QuerySelectField('Lecturer', query_factory=lecturer_query, allow_blank=True, get_label="full_name", get_pk=get_pk)
    students = QuerySelectMultipleField(query_factory=app.Student.query.all, get_label="name", get_pk=get_pk)
    submit = SubmitField('Pridėti paskaitą')
    
class LecturerForm(FlaskForm):
    name = StringField('Vardas', validators=[DataRequired(message='Įveskite vardą')])
    l_name = StringField('Pavardė', validators=[DataRequired(message='Įveskite pavardę')])
    lessons = QuerySelectMultipleField(query_factory=app.Lesson.query.all, get_label="name", get_pk=get_pk)
    submit = SubmitField('Pridėti dėstytoją')
    