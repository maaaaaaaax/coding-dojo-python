# with every Flask application, first import the Flask module
from flask import Flask, render_template
# create a variable called app, and set it equal to an instance of the Flask module
app = Flask(__name__)

# create a decorator, which attaches a function to a specific route
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
@app.route('/')
# define a function
# when our server is started and we visit localhost:5000, the default route for our application, it will call this function
def hello_world():
    return render_template('index.html')

@app.route('/success')
def success():
  return render_template('success.html')

# we're going to run our application, that we defined earlier, and we're going to run it in debug mode, which will print errors
app.run(debug=True)

# run a server by typing python and the flask file name into the terminal, in this case:
# $ python hello.py

# go to Chrome and type in localhost:5000 to the address bar
# Ctrl C in terminal to quit the server
