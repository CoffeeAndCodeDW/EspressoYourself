import csv
with open('EspressoYourself.csv', newline='') as csvfile:
	espresso = csv.reader(csvfile, delimiter=',', quotechar='|')

	for row in espresso :
		print(row[10])

	#while 1 == 1 : 
	#	newlist = next(filereader)
	#	for i in range(18) :
	#		print(newlist[i])
		