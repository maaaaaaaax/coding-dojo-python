from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# print mysql.query_db("SELECT * FROM users")
print mysql.query_db("SELECT users.name FROM users")[1]["name"] # output is Michael, or the users.name where ID is 2
app.run(debug=True)
