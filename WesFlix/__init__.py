from flask import Flask
from flask import render_template

app = Flask(__name__)

# Initialize blueprints

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calendar')
def calendar():
	return render_template('calendar.html')
@app.route('/contact')
def contact():
  return render_template('contact.html')
@app.route('/blade_runner')
def blade_runner():
  return render_template('Blade Runner.html')
@app.route('/dirty_harry')
def dirty_harry():
  return render_template('Dirty Harry.html')
@app.route('/doubt')
def doubt():
  return render_template('Doubt.html')
@app.route('/five_broken_cameras')
def five_broken_cameras():
  return render_template('Five Broken Cameras.html')
@app.route('/futurama')
def futurama():
  return render_template('Futurama.html')
@app.route('/jurassic_world')
def jurassic_world():
  return render_template('Jurassic World.html')
@app.route('/shawshank_redemption')
def shawshank_redemption():
  return render_template('Shawshank Redemption.html')
@app.route('/the_philadelphia_story')
def the_philadelphia_story():
  return render_template('The Philadelophia Story.html')
if __name__ == '__main__':
    app.run()
