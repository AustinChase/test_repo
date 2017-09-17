with open("Source_Data_v2.csv", "r") as my_file:
	import csv
	my_list.remove(my_list[1])
	csvReader = csv.DictReader(my_file)
	print csvReader.fieldnames
	my_list = []
	for row in csvReader:
	    entry = {}
	    for fieldname in csvReader.fieldnames:
	        entry[fieldname] = row[fieldname]
	    my_list.append(entry)