import csv
with open('', newline='') as csvfile:
	spamreader = csv.reader(cvsfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print(', '.join(row))