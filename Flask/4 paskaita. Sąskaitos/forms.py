from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField
import app



class UserForm(FlaskForm):
    name = StringField('Vardas', validators=[DataRequired(message='Įveskite vardą')])
    l_name = StringField('Pavardė', validators=[DataRequired(message='Įveskite pavardę')])
    code = IntegerField('Asmens kodas', validators=[DataRequired(message='Įveskite asmens kodą')])
    phone_number = StringField('Telefono numeris', validators=[DataRequired(message='Įveskite telefono numerį')])
    submit = SubmitField('Pridėti asmenį')
    
class BankForm(FlaskForm):
    bank_name = StringField('Pavadinimas', validators=[DataRequired(message='Įveskite banko pavadinimą')])
    address = StringField('Adresas', validators=[DataRequired(message='Įveskite banko adresą')])
    bank_code = StringField('Banko kodas', validators=[DataRequired(message='Įveskite banko kodą')])
    swift = StringField('SWIFT kodas', validators=[DataRequired(message='Įveskite SWIFT kodą')])
    submit = SubmitField('Pridėti banką')
    
def user_query():
    return app.User.query

def bank_query():
    return app.Bank.query

def get_pk(obj):
    return str(obj)
    
class AccountForm(FlaskForm):
    number = StringField('Sąskaitos numeris', validators=[DataRequired(message='Įveskite sąskaitos numerį')])
    balanse = IntegerField('Balansas', validators=[DataRequired(message='Įveskite sąskaitos balansą')])
    bank = QuerySelectField('Bankas', query_factory=bank_query, allow_blank=True, get_label="bank_name", get_pk=get_pk)
    user = QuerySelectField('Savininkas', query_factory=user_query, allow_blank=True, get_label="l_name", get_pk=get_pk)
    submit = SubmitField('Pridėti sąskaitą')