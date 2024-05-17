from flask import Flask, render_template, redirect, request
from forms import LeadForm
from utils import works

app = Flask(__name__)
app.config['SECRET_KEY'] = '123' # move this to .env file later

@app.route('/')
def test():
  return 'Hello World'

@app.route('/form', methods=['GET', 'POST'])
def lead_form():
  form = LeadForm()
  if form.is_submitted(): # create an is_submitted function to verify that all form inputs are valid
    result = request.form
    print(works())
    return redirect('/success')
  return render_template('leadform.html', form=form)

@app.route('/success')
def submitted_form():
  return render_template('submitted.html')

if __name__ == '__main__':
  app.run()