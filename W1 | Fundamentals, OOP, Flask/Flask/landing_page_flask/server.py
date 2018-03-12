# with every Flask application, first import the Flask module
from flask import Flask, render_template
# create a variable called app, and set it equal to an instance of the Flask module
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/ninjas')
def ninjas():
  return render_template("ninjas.html")

@app.route('/dojos/new')
def dojo():
  return render_template("dojos_new.html")

# we're going to run our application, that we defined earlier, and we're going to run it in debug mode, which will print errors
app.run(debug=True)
