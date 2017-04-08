import csv
import sqlite3

conn = sqlite3.connect('espresso.db')
print(conn)
c = conn.cursor()

teams = [] 
indivs = []
with open('EspressoYourself.csv', newline='') as csvfile:
	espresso = csv.reader(csvfile, delimiter=',', quotechar='|')

	next(espresso)

	for row in espresso :
		curr_team = {
			"name" : row[1].lower(), 
			"size" : row[2], 
			"mentor" : row[3], 
			"project" : row[4], 
			"languages" : row[5],
			}
		can_append = True
		for team in teams :
			if curr_team["name"] == team["name"] :
				can_append = False
		if can_append :
			teams.append(curr_team)

		curr_indiv = {
			"name" : row[6],
			"major" : row[7],
			"year" : row[8],
			"hometown" : row[9],
			"race" : row[10],
			"languages" : row[11],
			"gender" : row[12],
			"hobbies" : row[13],
			"coded" : row[14],
			"prog_langs" : row[15],
			"spot" : row[16],
			"role_model" : row[17],
			"pineapple" : row[18],
			"coffee_order" : row[19],
			"team" : row[1].lower(),
		}
		indivs.append(curr_indiv)

for team in teams :
	c.execute("INSERT INTO teams (team, size, mentor, project, languages) VALUES (?, ?, ?, ?, ?)", (team["name"], int(team["size"]), team["mentor"], team["project"], team["languages"]))

for indiv in indivs :
	c.execute("INSERT INTO individuals (name, major, year, hometown, race, languages, gender, hobbies, coded, prog_langs, spot, role_model, pineapple, coffee_order, team) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (indiv["name"], indiv["major"], indiv["year"], indiv["hometown"], indiv["race"], indiv["languages"], indiv["gender"], indiv["hobbies"], indiv["coded"], indiv["prog_langs"], indiv["spot"], indiv["role_model"], indiv["pineapple"], indiv["coffee_order"], indiv["team"]))

print(c.execute("SELECT mentor from teams WHERE id = 1").fetchall()[0][0])
print(c.execute("SELECT name from individuals WHERE id = 1").fetchall())
#for indiv in indivs :
#	print(indiv)


	#while 1 == 1 : 
	#	newlist = next(filereader)
	#	for i in range(18) :
	#		print(newlist[i])
		