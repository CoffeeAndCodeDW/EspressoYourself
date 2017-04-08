from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

def connect_db(): 
	return sqlite3.connect('espresso.db')

def disconnect_db(connection):
	connection.close() 

def get_teams():
	conn = connect_db()
	c = conn.cursor()
	teams = c.execute("SELECT * from teams")
	return teams.fetchall()

def get_individuals(team): 
	conn = connect_db()
	c = conn.cursor()
	people = c.execute("SELECT * from individuals WHERE team = (?)", (team,))
	return people.fetchall()

@app.route("/")
def hello():
    return "Welcome to Espresso Yourself! <br> Please excuse our mess."

@app.route("/teams")
def list_of_teams():
	teams = get_teams()
	team_lst = []
	for team in teams: 
		team_lst.append(team[1])
	return "Teams: <br><br>" + "<br>".join([str(x) for x in team_lst])

@app.route("/teams/<team>")
def team_page(team):
	gals = get_individuals(team)
	return "Members: <br><br>" + "<br>".join([str(x) for x in gals])

if __name__ == "__main__":
    app.run()