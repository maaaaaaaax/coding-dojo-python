from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/survey_submit', methods=['POST'])
def submit():
    print "Got Post Info"

    if len(request.form['name']) < 1:
        flash("Name cannot be blank!")
    elif len(request.form['comment']) < 1:
        flash("Comment cannot be blank!")
    elif len(request.form['comment']) > 120:
        flash("Comment cannot be more than 120 characters.")
    else:
        flash("Success!")

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    print "Name: {}".format(name)
    print "Location: {}".format(location)
    print "Language: {}".format(language)
    print "Comment: {}".format(comment)

    return render_template("result.html", name=name, location=location, language=language, comment=comment)
    #
    # return redirect('/')

# @app.route('/result')
# def result():
#    return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True) # run our server
