from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField

class LeadForm(FlaskForm):
  first_name = StringField('First Name')
  last_name = StringField('Last Name')
  company_name = StringField('Company Name')
  email = EmailField('Email')
  submit = SubmitField('Submit')
