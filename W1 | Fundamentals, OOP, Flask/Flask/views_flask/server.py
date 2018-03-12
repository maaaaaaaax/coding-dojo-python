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
    return render_template("index.html", name="Jay")

# When you run the app you will see that {{name}} in the HTML file was replaced by the variable that we passed to the render_template function! Flask uses a templating engine called Jinja2 to parse through files looking for {{}}, replace variables with real values, and send a complete HTML file back to the client.
app.run(debug=True)
