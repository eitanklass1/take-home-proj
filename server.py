from flask import Flask, render_template, redirect, request
from forms import LeadForm
from flask_mail import Mail, Message
import os
from utils import populate_email

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
    # function to send email here
    # populate_email(result)
    msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["eitan.klass@gmail.com"], # replace with your email for testing
                      body="This is a test email I sent with Gmail and Python!")
    mail.send(msg)
    return redirect('/success')
  return render_template('leadform.html', form=form)

@app.route('/success')
def submitted_form():
  return render_template('submitted.html')

if __name__ == '__main__':
  app.run(debug=True)