from flask import Flask, render_template, request, redirect, session
import random # import the random module
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# our index route will handle rendering our form
@app.route('/')
def index():
    if "random_number" not in session:
        session['random_number'] = random.randrange(0, 101) # random number between 0-100
        session['display_guess'] = "none"
    print session['random_number']
    return render_template("index.html")

@app.route('/submit_guess', methods=['POST'])
def guess():
    print "Got Post Info"
    # if the user has guessed correctly, tell the user as much
    if int(request.form['guess']) == int(session['random_number']):
        session['display_guess'] = "correct"
    # if the user has guessed too high, tell the user as much
    elif int(request.form['guess']) > int(session['random_number']):
        session['display_guess'] = "high"
    # if the user has guessed too low, tell the user as much
    else:
        session['display_guess'] = "low"
    return redirect('/')

@app.route('/reset')
def reset():
    # reset the random number and redirect to the home page
    session['display_guess'] = "none"
    session['random_number'] = random.randrange(0, 101) 
    return redirect('/')

app.run(debug=True) # run our server
