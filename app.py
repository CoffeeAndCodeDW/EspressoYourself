from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

def connect_db(): 
	return sqlite3.connect('espresso.db')

def disconnect_db(connection):
	connection.close() 

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/teams/<team>")
def team_page(team):
	return team

if __name__ == "__main__":
    app.run()