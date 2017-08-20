# This file is a collection of notes to:
#   a)  recreate the environment we got to
#   b) conceptualize what to do next

# the task we were working on was getting your work's csv folder into a python digestable format
# the file was in your project folder called source_data_v2.csv

# First and foremost,  remember to go to your project folder then activate the virtual environment
# the terminal command for virtual environment is . ./venv/bin/activate
# then you can go into ipython

# now we need to import the one requirement for this is
import csv

# One extra thing we never went over is getting you this list into a variable.
# Im creating this function so that you can pull this list out without having to copy and paste this logic.
# to do this,  make sure you have this script in your working directory, the do the following

# from csv_data_to_python import gimme_data
# my_data = gimme_data()


def gimme_data():
    # lets initialize a list of lists and a list of dictionaries to give you two options to play with the data with
    lsf_list_of_lists = []
    lsf_list_of_dicts = []

    # lets start with the list
    # the "with" statement is just pythons weird way of opening files or connections to close them later.
    with open('source_data_v2.csv') as csvfile:
        # "csvfile" is the variable name we are given this open file
        reader = csv.reader(csvfile)
        for row in reader:
            lsf_list_of_lists.append(row)

        # each row is a list of values.  the lsf_list is a list of these lists.  (like a meta list)
        # if you look at the csv, you could see the first TWO rows are headers for the column.
        # do with that what you will.  You could grab each one by saying lsf_list[0] lsf_list[1]

        # now lets do it with as a dictionary.  our file is still open because we are in the with loop.
        # an optional argument you can give is fieldnames=[<list of words you want for keys>]
        dict_reader = csv.DictReader(csvfile)
        for row in dict_reader:
            lsf_list_of_dicts.append(row)

        # this will give you a list of dictionaries
        # {'name': 'austin', 'age': 5}

    # either of these ways works. the second one might be easier to work  with since you can do things like:
    # row['company_name'] == 'Farella Braun'  # True

    return lsf_list_of_dicts
