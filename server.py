from flask import Flask, render_template, redirect, request
from forms import LeadForm
from flask_mail import Mail
import os
from utils import populate_email
from crm_access import create_contact

app = Flask(__name__)
app.config['SECRET_KEY'] = '123' # move this to .env file later

mail_settings = {
  "MAIL_SERVER": 'smtp.gmail.com',
  "MAIL_PORT": 465,
  "MAIL_USE_TLS": False,
  "MAIL_USE_SSL": True,
  "MAIL_USERNAME": os.getenv('EMAIL_USER'),
  "MAIL_PASSWORD": os.getenv('EMAIL_PASSWORD')
}

app.config.update(mail_settings)
mail = Mail(app)

@app.route('/')
def test():
  return 'Hello World'

@app.route('/form', methods=['GET', 'POST'])
def lead_form():
  form = LeadForm()
  if form.is_submitted():
    result = request.form
    mail.send(populate_email(result))
    create_contact(result)
    return redirect('/success')
  return render_template('leadform.html', form=form)

@app.route('/success')
def submitted_form():
  return render_template('submitted.html')

if __name__ == '__main__':
  app.run(debug=True)