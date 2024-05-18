from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, validators

class LeadForm(FlaskForm):
  first_name = StringField('First Name', [
    validators.Length(min=2, max=25),
    validators.InputRequired()
  ])
  last_name = StringField('Last Name', [
    validators.Length(min=2, max=25),
    validators.InputRequired()
  ])
  company_name = StringField('Company Name', [
    validators.Length(min=2, max=25),
    validators.InputRequired()
  ])
  email = EmailField('Email', [
    validators.InputRequired()
  ])
  submit = SubmitField('Submit')
