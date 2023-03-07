from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, InputRequired
    
class ContactForm(FlaskForm):
    email = StringField('Email', [Email(message=('Incorrect email')), DataRequired(message='Required')])
    password = PasswordField('Password', validators=[DataRequired(message='Required'), EqualTo('confirm_password', message='Passwords must match'), Length(min=8, message=('Must be 8 or more symbols'))])
    confirm_password = PasswordField('Confirm_password', validators=[DataRequired(message='Required')])
    address1 = TextAreaField('Address1', [Optional(), Length(max=200)])
    address2 = TextAreaField('Address2', [Optional(), Length(max=200)])
    city = SelectField('City', choices=[('Vilnius'), ('Kaunas'), ('Klaipėda')], validators=[DataRequired(message='Required')])
    state = StringField('State', [Optional()])
    zip_code = StringField('Zip_Code', [DataRequired(message='Required')])
    agree =  BooleanField('Agree', [DataRequired(message='Required')])
    submit = SubmitField('Submit')