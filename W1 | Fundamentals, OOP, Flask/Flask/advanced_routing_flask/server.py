# Passing data from the client to the server through the URL

# What if we wanted to have a route '/users/___' where anything that comes after '/users/' was passed as a variable to the route handler. If we could do this then we could have '/users/jay' display a page that says "Hello Jay" and '/users/anna' display a page that says "Hello Anna" without writing two different route handlers!

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# @app.route('/users/<username>')
# def show_user_profile(username):
#     print username
#     return render_template("user.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users/<username>/')
def show_user_profile(username):
    print username
    return render_template("user.html")

@app.route('/users/<username>/<ID>')
def show_user_profile_with_id(username, ID):
    print username
    print ID
    return render_template("user.html")

app.run(debug=True)
