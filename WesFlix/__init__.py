from flask import Flask
from flask import render_template

app = Flask(__name__)

# Initialize blueprints

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/template')
def template():
  return render_template('template.html')
@app.route('/contact')
def contact():
  return render_template('contact.html')
if __name__ == '__main__':
    app.run()
