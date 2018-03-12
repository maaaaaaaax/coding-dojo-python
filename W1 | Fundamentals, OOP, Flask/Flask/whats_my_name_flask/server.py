from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/users', methods=['POST'])
def create_user():
   print "Got Post Info"
   # The name we gave to each HTML input was significant. On the server-side, we can access data that was input into a field from a user through the request.form dictionary by providing the name of the input as the key.
   # The type of anything that comes in through request.form will be "String" no matter what. If you want that value to be identified as an actual number you'll have to type cast it.
   name = request.form['name']
   # redirects back to the '/' route
   print "Name: {}".format(name)
   return redirect('/')

app.run(debug=True) # run our server
