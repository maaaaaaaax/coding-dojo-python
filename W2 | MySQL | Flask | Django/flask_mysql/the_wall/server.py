from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re, md5, os, binascii  # tools for email validation and password hashing
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app,'flask_the_wall')

@app.route('/')
def index():
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
        flash("The email you provided is already in use.")
        print "The email you provided is already in use."
        return render_template('index.html', old_form=request.form)
    else:
        print "New email: {}".format(session['test_email'])

    # test password for length (at least 6) and match
    if len(request.form['password']) < 6 or request.form['password'] != request.form['password_confirm']:
        flash("Passwords must be at least 6 characters and must match.")
        print "Passwords must be at least 6 characters and must match."
        return render_template('index.html', old_form=request.form)

    # create hashed password and salt
    password = request.form['password']
    hashed_salt = binascii.b2a_hex(os.urandom(15))
    hashed_pw = md5.new(password + hashed_salt).hexdigest()

    # IF NO ERRORS:
    # insert the new user info into the database and store their user info in session as a logged in user
    query = "INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, :salt, NOW(), NOW())"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw,
            'salt': hashed_salt
           }
    mysql.query_db(query, data)

    print "Inserted successsfully"

    # store their user info in session
    query = "SELECT * from users WHERE email=:test_email"
    data = {'test_email': session['test_email']}
    session['current_user'] = mysql.query_db(query, data)
    print "session['current_user'] is ", session['current_user'][0]['email']

    session['source'] = "sign_up"

    return redirect('/wall')

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

    # if email pasts initial tests, store email in session
    session['test_email'] = request.form['email_sign_in']

    # check password
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

        query = "SELECT * from users WHERE email=:test_email"
        data = {'test_email': session['test_email']}
        session['current_user'] = mysql.query_db(query, data)
        print "session['current_user'] is ", session['current_user'][0]['email']
        session['source'] = "sign_in"
        return redirect('/wall')

@app.route('/wall')
def show():
    # Write query to select all posts and comments
    all_posts = mysql.query_db("SELECT * from posts JOIN users ON users.users_id = posts.user_id")
    # print "All posts: ", all_posts
    all_comments = mysql.query_db("SELECT * from comments JOIN posts ON posts.posts_id = comments.post_id JOIN users on users.users_id = comments.user_id")
    # print "All comments: ", all_comments
    # for post in all_posts:
    #     print "Message author: {} {}".format(post['first_name'], post['last_name'])
    #     print post['message']
    #     for comment in all_comments:
    #         if comment['post_id'] == post['posts_id']:
    #             print "Comment author: {} {}".format(comment['first_name'], comment['last_name'])
    #             print comment['comment']

    return render_template('wall.html', all_posts=all_posts, all_comments=all_comments)


@app.route('/submit_post', methods=['POST'])
def submit_post():

    # error checking for form submission - length has to be at least 1
    if len(request.form['content']) < 1:
        flash("Post cannot be blank.")
        print "Post cannot be blank."
        return redirect('/wall')
    print "session['current_user'][0]['email'] is {}".format(str(session['current_user'][0]['email']))
    data = {
        'message': str(request.form['content']),
        'user_id': int(session['current_user'][0]['users_id'])
    }
    print "Querying database"
    query = "INSERT INTO posts (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    mysql.query_db(query,data)
    print "Success: added {} as a new message to the database.".format(request.form['content'])
    return redirect('/wall')

@app.route('/submit_comment', methods=['POST'])
def submit_comment():

    # error checking for form submission - length has to be at least 1
    if len(request.form['content']) < 1:
        flash("Comment cannot be blank.")
        print "Comment cannot be blank."
        return redirect('/wall')
    # print "session['current_user'][0]['email'] is {}".format(str(session['current_user'][0]['email']))
    print "request.form['post_id'] is: {}".format(request.form['post_id'])
    data = {
        'message': str(request.form['content']),
        'user_id': int(session['current_user'][0]['users_id']),
        'post_id': int(request.form['post_id'])
    }
    print "Querying database"
    # query = "INSERT INTO comments (post_id, user_id, comment, created_at, updated_at) VALUES (:post_id, :user_id, :comment, NOW(), NOW())"
    query = "INSERT INTO `flask_the_wall`.`comments` (`post_id`, `user_id`, `comment`, `created_at`, `updated_at`) VALUES (:post_id, :user_id, :message, NOW(), NOW())"
    mysql.query_db(query,data)
    print "Success: added {} as a new comment to post {} to the database.".format(request.form['content'], request.form['post_id'])
    return redirect('/wall')

## ADD THE MESSAGE ID TO THIS
# @app.route('/submit_comment', methods=['POST'])
# def submit_comment():
#
#     # error checking for form submission - length has to be at least 1
#     if len(request.form['content']) < 1:
#         flash("Post cannot be blank.")
#         print "Post cannot be blank."
#         return redirect('/wall')
#     print "session['current_user'][0]['users_id'] is {}".format(int(session['current_user'][0]['users_id']))
#     data = {
#         'message': str(request.form['content']),
#         'user_id': int(session['current_user'][0]['users_id'])
#     }
#     print "Querying database"
#     query = "INSERT INTO posts (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
#     mysql.query_db(query,data)
#     print "Success: added {} as a new comment to the database.".format(request.form['content'])
#     return redirect('/wall')

@app.route('/log_out', methods=['POST'])
def log_out():
    print "Cleared session"
    session.clear()
    flash("You have logged out.")
    return redirect('/')

app.run(debug=True)
