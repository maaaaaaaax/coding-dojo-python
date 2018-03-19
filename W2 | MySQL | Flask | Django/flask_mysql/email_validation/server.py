from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'emails')

@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM emails")
    # print friends
    return render_template('index.html', all_emails=emails)

@app.route('/submit', methods=['POST'])
def submit():

    if len(request.form['email']) < 1:
        flash("Name cannot be blank!")
        print "Name cannot be blank!"
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect ('/')

    query = "SELECT email from emails where email=:test_email"
    data = {'test_email': request.form['email']}
    query_result = mysql.query_db(query, data)
    print query_result
    if query_result:
        flash("We already have this email in our database.")
        print "We already have this email in our database."
        return redirect('/')

    print "Got Post Info"
    session['email'] = request.form['email']
    print "Email: {}".format(session['email'])
    print session['email']

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': request.form['email'],
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/success')

@app.route('/success')
def show():
    # Write query to select all emails
    query = "SELECT * FROM emails"
    query_result = mysql.query_db(query)
    # print query_result
    return render_template('success.html', all_emails=query_result, new_email=session['email'])


app.run(debug=True)
