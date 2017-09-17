import csv
# always put the import functions at the top of your file
# it helps when you're debugging to find what modules could be breaking


with open("Source_Data_v2.csv", "r") as my_file:
    # print csvReader.fieldnames
    csvReader = csv.DictReader(my_file)
    my_list = []
    for row in csvReader:
        entry = {}
        for fieldname in csvReader.fieldnames:
            entry[fieldname] = row[fieldname]
        my_list.append(entry)
return my_list

# this line is what you use whenever you want your script to be run wihtout ipython.
# if you pull this code into an environment (ie import code.parse)
# it will not call this stuff,  because __name__ wont be __main__.
if __name__ == '__main__':
    print "there are {} rows in my file".format(len(my_list))
    print "there are {} columns in my file".format(len(csvReader.fieldnames))
    print "I was called as a script!!"
