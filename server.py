from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def test():
  return 'Hello World'

@app.route('/form')
def form():
  return render_template('form.html')

@app.route('/form-submitted')
def submitted_form():
  return render_template('submitted.html')

if __name__ == '__main__':
  app.run()