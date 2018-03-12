from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        return render_template("ninja_blue.html")
    if color == "orange":
        return render_template("ninja_orange.html")
    if color == "red":
        return render_template("ninja_red.html")
    if color == "purple":
        return render_template("ninja_purple.html")
    else:
        return render_template("not_a_ninja.html")

app.run(debug=True) # run our server
