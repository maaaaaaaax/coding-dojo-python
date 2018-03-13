# In this example, we will learn how to pass data between routes. Currently, we have a route that handles the form submit but it doesn't do anything with that data in terms of presenting it to the view.
#
# First, let's create a route in our form_test project that serves a page and supplies the page with a name and email to display.


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    # The name we gave to each HTML input was significant. On the server-side, we can access data that was input into a field from a user through the request.form dictionary by providing the name of the input as the key.
    # The type of anything that comes in through request.form will be "String" no matter what. If you want that value to be identified as an actual number you'll have to type cast it.
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    # print "Name: {}".format(name)
    # print "Email: {}".format(email)
    # redirects back to the '/' route
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html')

# # Submitting the form takes you to the POST /users route which is handled by the create_user function where we store the POST data in session
# The create_user function then redirects you to the GET /show route which is handled by the show_user function where we render the user.html template passing along the necessary information to the view

# Session is a way to store information unique to a particular client
# Session uses cookies to store some or all of the required information
# When you want to access and modify data over multiple redirects use session
# You can use session in both your server.py file as well as your templates
# Even though you have access to the session, you should not abuse the amount of information you store in it. Store only what you need in the session. Once we incorporate a database you should be limiting what you store in sessions to the most minimal amount of data possible.


app.run(debug=True) # run our server
