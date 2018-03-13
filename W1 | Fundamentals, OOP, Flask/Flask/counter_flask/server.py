# In this example, we will learn how to pass data between routes. Currently, we have a route that handles the form submit but it doesn't do anything with that data in terms of presenting it to the view.
#
# First, let's create a route in our form_test project that serves a page and supplies the page with a name and email to display.

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'



# our index route will handle rendering our form
@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
    else:
        session['counter'] = session['counter'] + 1
    return render_template("index.html")

app.run(debug=True) # run our server
