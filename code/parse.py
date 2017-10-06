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

def get_copay():

# call the parse data function
    my_data = parse_csv()
# create an empty list to store the clean Rx data
    non_kaiser_Rx = []
# cycle through dictionaries and pull out Q121_3_1, filter out any blanks
    for items in my_data:
        non_kaiser_Rx.append(items['Q121_3_1'])
        non_kaiser_Rx = filter(None, non_kaiser_Rx)
 #remove first descriptor variable  
    non_kaiser_Rx.remove(non_kaiser_Rx[0])
    
    sum = 0
    counter = len(non_kaiser_Rx)
    average = 0
 #calculate average   
    for copay in non_kaiser_Rx:
        copay = int(copay)
        sum = sum + copay

    average = sum / counter

    return average, " 1 "

if __name__ == '__main__':
    calced_data = get_copay()
    print  "The average non Kaiser HMO Rx copay is $%s" %calced_data

def get_enrollment_HMO_non_kaiser():
    my_data = parse_csv()
    enrollment_non_kaiser = []
# populate empty list with raw enrollment data for Non Kaiser HMO
    for items in my_data:
        enrollment_non_kaiser.append(items['Q63_1'])
 # remove the first row in the list, the questions' description       
    enrollment_non_kaiser.remove(enrollment_non_kaiser[0])
# use list comprehension to replace None types and/or string blanks with 0s
    enrollment_non_kaiser = [0 if v is '' or None else v for v in enrollment_non_kaiser]
    return enrollment_non_kaiser

def get_enrollment_HMO_kaiser():
# same code as get_enrollment_HMO_non_kaiser, just adding HMO_kaiser     
    my_data = parse_csv()
    enrollment_kaiser = []
    # populate empty list with raw enrollment data for Kaiser HMO
    for items in my_data:
        enrollment_kaiser.append(items['Q63_2'])

    enrollment_kaiser.remove(enrollment_kaiser[0])

    enrollment_kaiser = [0 if v is '' or None else v for v in enrollment_kaiser]    
    
    return enrollment_kaiser

def get_enrollment_PPO():
 # same code as above, just adding PPO   
    my_data = parse_csv()
    enrollment_PPO = []

    for items in my_data:
        enrollment_PPO.append(items['Q63_3'])

    enrollment_PPO.remove(enrollment_PPO[0]) 

    enrollment_PPO = [0 if v is '' or None else v for v in enrollment_PPO]

    return enrollment_PPO

def get_enrollment_HDHP():
 # same code as above, just adding PPO   
    my_data = parse_csv()
    enrollment_HDHP = []

    for items in my_data:
        enrollment_HDHP.append(items['Q63_3'])

    enrollment_HDHP.remove(enrollment_HDHP[0]) 

    enrollment_HDHP = [0 if v is '' or None else v for v in enrollment_HDHP]

    return enrollment_HDHP

def get_enrollment_waiver():
 # same code as above, just adding PPO   
    my_data = parse_csv()
    enrollment_waiver = []

    for items in my_data:
        enrollment_waiver.append(items['Q63_3'])

    enrollment_waiver.remove(enrollment_waiver[0]) 

    enrollment_waiver = [0 if v is '' or None else v for v in enrollment_waiver]

    return enrollment_waiver

def get_average_enrollment(eHMO, eKHMO, ePPO, eHDHP, eWaiver):
    my_list = [eHMO,eKHMO, ePPO, eHDHP, eWaiver]
    enrollment_sum = 0
    enrollment_sums = [0,0,0,0,0]
    average_enrollment = [0,0,0,0,0]
    i = 0
    a = 0
    counter = 0
    # loop through lists of enrollments for each product type
    for e_list in my_list:
        # loop through each value of each list
        for item in e_list:
            # convert string types to floats and sum values by product
            enrollment_sum = float(item) + enrollment_sum
            # create new list for sums
            enrollment_sums[i] = enrollment_sum
        # increment counter for outside loop    
        i += 1
        
    # loop through new list of sums
    for subtotal in enrollment_sums:
        # calculate lench of each original list
        counter = len(my_list[a])
        # populate new list with average enrollemnts
        average_enrollment[a] = enrollment_sums[a] / counter
        #increment loop
        a += 1
    # return list of averages    
    return average_enrollment

if __name__ == 'main':
    calced_enrollment = get_enrollment_HMO_non_kaiser()
    print "Work in progress, returning a scrubbed enrollment list: %s" %calced_enrollment   
# this function takes a single argument and writes the argument to a new csv file
def write_data(answers):
    with open('data_inputs.csv','wb') as csvfile:
        my_writer = csv.writer(csvfile, delimiter = ' ')
        my_writer.writerow(answers)
    return













