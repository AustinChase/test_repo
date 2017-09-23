import csv
# always put the import functions at the top of your file
# it helps when you're debugging to find what modules could be breaking


def parse_csv():
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
    grabbed_data = parse_csv()
    print "there are {} rows in my file".format(len(grabbed_data))
    print "there are {} columns in my file".format(len(grabbed_data[0].keys()))
    print "I was called as a script!!"


def get_non_kaiser_copay():

# call the parse data function
    my_data = parse_csv()
# create an empty list to store the clean Rx data
    non_kaiser_Rx = []
# cycle through dictionaries and pull out Q121_3_1, filter out any blanks
    for items in my_data:
        non_kaiser_Rx.append(items['Q121_3_1'])
        non_kaiser_Rx = filter(None, non_kaiser_Rx)
 #remove first disciptor variable since it breaks the int function   
    non_kaiser_Rx.remove(non_kaiser_Rx[0])
    
    sum = 0
    counter = len(non_kaiser_Rx)
    average = 0
 #calculate average   
    for copay in non_kaiser_Rx:
        copay = int(copay)
        sum = sum + copay

    average = sum / counter

    return "The average non Kaiser HMO Rx copay is $%s" %(average)

if __name__ == '__main__':
    print get_non_kaiser_copay()   







