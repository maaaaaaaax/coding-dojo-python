# Setting up
# virtual environments are a tool for creating unique sandboxes to control project dependencies
# If you haven't already installed virtualenv, do that now! Run this command:

pip install virtualenv

# Now create a new virtual environment in this folder. In this example, we named our environment with the python version (2), and the major dependency (Flask)

virtualenv flaskEnv

# You should now see a new folder created in the myEnvironments directory called flaskEnv. Note the directory created reflects the argument (flaskEnv) that was passed to the virtualenv command.

# Activating your virtualEnvironments
# While in the parent directory to our virtual environments (myEnvironments), activate the virtual environment by typing:

source flaskEnv/bin/activate

# Your terminal/command prompt should change and look something like this:
# (flaskEnv) $

# To deactivate your virtual environment, just type deactivate in the command line. Closing your terminal window will deactivate your virtual environment. If you do so, simply activate it again.


# with every Flask application, first import the Flask module
from flask import Flask
# create a variable called app, and set it equal to an instance of the Flask module
app = Flask(__name__)

# create a decorator, which attaches a function to a specific route
# The "@" symbol designates a "decorator" which attaches the following function to the '/' route. This means that whenever we send a request to localhost:5000/ we will run the following "hello_world" function.
# A route is much like a variable name we assign to a request. The job of a route is to communicate to the server what kind of information the client needs.
@app.route('/')
# define a function
# when our server is started and we visit localhost:5000, the default route for our application, it will call this function
def hello_world():
    return "Hello, World!"

# we're going to run our application, that we defined earlier, and we're going to run it in debug mode, which will print errors
app.run(debug=True)

# run a server by typing python and the flask file name into the terminal, in this case:
# $ python hello.py

# go to Chrome and type in localhost:5000 to the address bar
# Ctrl C in terminal to quit the server

# We are going to add a templates directory alongside our hello.py file. Inside the templates directory, add this index.html file:
#
# /hello_flask/templates/index.html


# Passing data from the client to the server through the URL

# What if we wanted to have a route '/users/___' where anything that comes after '/users/' was passed as a variable to the route handler. If we could do this then we could have '/users/jay' display a page that says "Hello Jay" and '/users/anna' display a page that says "Hello Anna" without writing two different route handlers!

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")
app.run(debug=True)



# Let's go over the basic structure for getting variables from the URL:
@app.route('/route/with/<vararg>')
def handler_function(vararg):
  # here you can use the variable "vararg"
  # if you want to see what our argument looks like
  print vararg
  # we could do other things with this information from this point on such as:
  # use it to retrieve some records from the database
  # render a particular template


# You can pass as many variables as you like in the URL as long as they are all passed as parameters to the route handler function:

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
	print username
	print id
    return render_template("user.html")



## VIEWS

# Templates are HTML files that are interpreted by Flask and then served to the client. This is called rendering templates and every web development framework provides a way to render templates. Now, let's see how you can pass data to the template and display it dynamically!

<html>
  <head>
    <title>Template Test</title>
  </head>
  <body>
    <p>My name is {{name}}</p>
  </body>
</html>

# Now, in our hello_world function definition change the return statement to be:

return render_template("index.html", name="Jay")

# When you run the app you will see that {{name}} in the HTML file was replaced by the variable that we passed to the render_template function! Flask uses a templating engine called Jinja2 to parse through files looking for {{}}, replace variables with real values, and send a complete HTML file back to the client.



# TEMPLATES

# There are 2 special inputs that we can use to insert Python-like code into our Flask templates. We should be clear that the code we can inject into templates is limited. We cannot use the full range of Python's functionality in our templates. Most of what you've learned so far can be used in your templates, but some of Python's more advanced functionality is missing.

{{ some variable }}
{% some expression %}

# Let's see this in action. First, create a new project directory called test_templates. Place a server.py file and a templates directory inside this directory.

Build a basic server.py file:
