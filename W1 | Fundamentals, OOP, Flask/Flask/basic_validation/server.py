from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecret'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['Post'])
def process():
    if len(request.form['name']) < 1:
        # display validation errors
        flash("Name cannot be empty!") # just pass a string to the flash function
    else:
        # display success message
        flash("Success! Your name is {}".format(request.form['name'])) # just pass a string to the flash function
    return redirect('/')

app.run(debug=True)

# Flask helps us with flash messages by giving us access to a function on the client side that allows us to get all flash messages as a list.
# This function is "get_flashed_messages()"
