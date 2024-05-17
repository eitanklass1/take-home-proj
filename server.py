from flask import Flask, render_template
from forms import LeadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '123' # move this to .env file later

@app.route('/')
def test():
  return 'Hello World'

@app.route('/form')
def lead_form():
  form = LeadForm()
  return render_template('leadform.html', form=form)

@app.route('/form-submitted')
def submitted_form():
  return render_template('submitted.html')

if __name__ == '__main__':
  app.run()