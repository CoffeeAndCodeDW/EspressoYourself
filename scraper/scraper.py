import csv
with open('EspressoYourself.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
	#for row in filereader:
		#print(' '.join(row))
	#for newS in filereader :
	#	for i in 18 :
	#		print newS.split(,)[i]

	while 1 == 1 : 
		newlist = next(filereader)
	#	for i in 18 :
	#		print(newlist[i])

		