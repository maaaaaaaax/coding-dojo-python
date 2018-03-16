from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii  # tools for email validation and password hashing
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'flask_login_and_registration')

@app.route('/')
def index():
    emails = mysql.query_db("SELECT * FROM users")

    if request.form:
        return render_template('index.html', old_form=request.form)

    return render_template('index.html', old_form=None)

@app.route('/sign_up', methods=['POST'])
def sign_up():

    # # error checking for form submission

    # first_name should be letters only, at least 2 characters and that it was submitted
    if len(request.form['first_name']) < 2 or request.form['first_name'].isalpha() is not True:
        flash("First name cannot be less than 2 characters and must be alphabetical.")
        print "First name cannot be less than 2 characters and must be alphabetical."
        return render_template('index.html', old_form=request.form)

    # last_name should be letters only, at least 2 characters and that it was submitted
    if len(request.form['last_name']) < 2 or request.form['last_name'].isalpha() is not True:
        flash("Last name cannot be less than 2 characters and must be alphabetical.")
        print "Last name cannot be less than 2 characters and must be alphabetical."
        return render_template('index.html', old_form=request.form)

    # email should be letters only, at least 2 characters and that it was submitted
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        print "Email cannot be blank!"
        return render_template('index.html', old_form=request.form)

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return render_template('index.html', old_form=request.form)

    # check if email is in database already ... if statement only triggers if the value is not NULL
    session['test_email'] = request.form['email']
    # print session['test_email']
    unique_email_db_query = "SELECT email from users WHERE email=:test_email"
    data = {'test_email': session['test_email']}
    query_result = mysql.query_db(unique_email_db_query, data)
    if query_result:
        flash("We already have this email in our database.")
        print "We already have this email in our database."
        return render_template('index.html', old_form=request.form)
    else:
        print "New email: {}".format(session['test_email'])

    # test password for length (at least 6) and match
    print request.form['password']
    print request.form['password_confirm']

    if len(request.form['password']) < 6 or request.form['password'] != request.form['password_confirm']:
        flash("Passwords must be at least 6 characters and must match.")
        print "Passwords must be at least 6 characters and must match."
        return render_template('index.html', old_form=request.form)

    # create hashed password and salt
    password = request.form['password']
    hashed_salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + hashed_salt).hexdigest()
    print "Salt: ", hashed_salt
    print "Hashed PW: ", hashed_pw

    # if no errors, insert the new user info into the database and store their email in session as a logged in user
    session['current_user_email'] = request.form['email']
    print "Got Post Info ... Inserting {} into DB".format(session['current_user_email'])

    # insert new user data into database
    query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw,
            'salt': hashed_salt
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)

    print "Inserted successsfully"

    session['source'] = "sign_up"

    return redirect('/success')

@app.route('/sign_in', methods=['POST'])
def sign_in():

    # error checking for form submission

    # email should be letters only, at least 2 characters and that it was submitted
    if len(request.form['email_sign_in']) < 1:
        flash("Email cannot be blank.")
        print "Email cannot be blank."
        return redirect('/')

    elif not EMAIL_REGEX.match(request.form['email_sign_in']):
        flash("Invalid Email Address.")
        return redirect ('/')

    session['test_email'] = request.form['email_sign_in']
    print session['test_email']

    # check if email is in database already ... if statement only triggers if the value is not NULL
    unique_email_db_query = "SELECT email from users WHERE email=:test_email"
    data = {'test_email': session['test_email']}
    query_result = mysql.query_db(unique_email_db_query, data)
    if not query_result:
        print "The provided email ({}) is not in our database. Please try another email.".format(session['test_email'])
        flash("The provided email ({}) is not in our database. Please try another email.".format(session['test_email']))
        return redirect('/')

    # if the email is found in the database, check if the passwords match
    if query_result:
        print "The provided email ({}) is in our database. Checking password".format(session['test_email'])
        session['test_password'] = request.form['password_sign_in']
        session['test_password_confirm'] = request.form['password_confirm_sign_in']
        if session['test_password'] != session['test_password_confirm']:
            print "Password does not match password confirm. Please enter the same password twice."
            flash("Password does not match password confirm. Please enter the same password twice.")
            return redirect('/')
        # test if the password for session['test_email'] is equal to session['test_password']
        query = "SELECT * from users where email=:test_email"
        data = { 'test_email': session['test_email'] }
        stored_user_data = mysql.query_db(query, data)
        print "Stored password: ", stored_user_data[0]['password']
        print "Provided password: ", session['test_password']

        ### NEW CODE BELOW

        if len(stored_user_data) != 0:
            encrypted_password = md5.new(session['test_password'] + stored_user_data[0]['salt']).hexdigest()
            if stored_user_data[0]['password'] == encrypted_password:
                print "Success! Hashed passwords match!"
            else:
                print "Hashed passwords don't match"
                flash("Password does not match password in our database. Please try again.")
                return render_template('index.html', old_form=request.form)
        # else:
        #     # invalid email!
        

        # if stored_user_data[0]['password'] != session['test_password']:
        #     print "wrong password"
        #     flash("Password does not match password in our database. Please try again.")
        #     return render_template('index.html', old_form=request.form)


        # print password_test_query
        # #output is [{u'password': u'password123'}]
        # print password_test_query[0]['password']
        # #output is password123
        # print "Password match"
        # session['current_user_info'] = password_test_query[0]
        # print session['current_user_id'][0]['first_name']
        session['current_user_info'] = stored_user_data
        print session['current_user_info']
        # #output is [{u'first_name': u'Max', u'last_name': u'Wiederholt', u'created_at': datetime.datetime(2018, 3, 15, 14, 49, 27), u'updated_at': datetime.datetime(2018, 3, 15, 14, 49, 27), u'email': u'max@max.com', u'password': u'password123', u'salt': u'456', u'id': 1L}]

        # print session['current_user_info'][0]['first_name']

        session['source'] = "sign_in"

        return redirect('/success')


@app.route('/success')
def show():
    # Write query to select all emails
    query = "SELECT * FROM users"
    query_result = mysql.query_db(query)
    # print query_result
    all_users = query_result
    return render_template('success.html', all_users=all_users)

@app.route('/log_out')
def log_out():
    print "Cleared session"
    session.clear()
    return redirect('/')

app.run(debug=True)
