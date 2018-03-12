from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/survey_submit', methods=['POST'])
def submit():
   print "Got Post Info"

   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']

   print "Name: {}".format(name)
   print "Location: {}".format(location)
   print "Language: {}".format(language)
   print "Comment: {}".format(comment)

   return render_template("result.html", name=name, location=location, language=language, comment=comment)

   # return redirect('/result')

# @app.route('/result')
# def result():
#    return render_template("result.html", name=name, location=location, language=language, comment=comment)

app.run(debug=True) # run our server
