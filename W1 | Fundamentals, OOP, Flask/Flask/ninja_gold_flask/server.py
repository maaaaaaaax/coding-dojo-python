# Create a simple game to test your understanding of flask, and implement the functionality below.
# For this assignment, you're going to create a mini-game that helps a ninja make some money! When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino) and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds. Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.

from flask import Flask, render_template, request, redirect, session, url_for
import random # import the random module

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['activity'] = ''
    session['score'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    output = ''
    if request.form['building'] == 'farm':
        session['farm'] = int(random.randrange(10,21))
        session['score'] += session['farm']
        output = 'Earned '+str(session['farm'])+' from farm!'
    elif request.form['building'] == 'cave':
        session['cave'] = int(random.randrange(5,11))
        session['score'] += session['cave']
        output = 'Earned '+str(session['cave'])+' from cave!'
    elif request.form['building'] == 'house':
        session['house'] = int(random.randrange(2,6))
        session['score'] += session['house']
        output = 'Earned '+str(session['house'])+' from house!'
    session['activity'] += "<p class='win'>"+output+"</p>"
    if request.form['building'] == 'casino':
        session['casino'] = int(random.randrange(-50,51))
        session['score'] += session['casino']
        if session['casino'] < 0:
            output = 'Entered a casino and lost '+str(session['casino'])+'...Ouch..'
            session['activity'] += "<p class='loss'>"+output+'</p>'
        else:
            output = 'Entered a casino and WON '+str(session['casino'])+'...Woohoo!!'
            session['activity'] += "<p class='win'>"+output+'</p>'

    return render_template('index.html', activity=session['activity'], score=session['score'])

app.run(debug=True) # run our server
