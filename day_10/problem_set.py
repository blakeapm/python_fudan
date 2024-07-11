###############################################################################
#                                                                             #
#                              Final Problem Set                              #
#                                                                             #
#                                                                             #
#                                                                             #
#   Welcome to the final problem set of the course! In this problem set, you  #
#   will be working with the FAA wildlife strikes dataset, which contains     #
#   data on aircraft strikes involving wildlife in the state of California.   #
#                                                                             #
#   Overall Objectives:                                                       #
#                                                                             #
#   1. To explore, clean, and analyze the FAA wildlife strikes dataset using  #
#   Python and pandas.                                                        #
#   2. To practice data manipulation, aggregation, and extraction techniques. #
#   3. To apply all that we have learned in the class toward a simple data    #
#   analysis task.                                                            #
#                                                                             #
#   Each question asks you to write some code to explore and describe certain #
#   attributes of the data.                                                   #
#                                                                             #
#   For each question block, please write code to perform the task you are    #
#   instructed to perform between the question blocks. Full points will only  #
#   be given for code that runs, so test your code by running your            #
#   problem_set.py in script mode with the command `python problem_set.py'.   #
#   When necessary please comment your code. When asked to write reflective   #
#   responses, please use triple quote comments.                              #
#                                                                             #
#   The number of points for each question is included in the problem blocks. #
#   Full points will be given to questions that produce expected outputs and  #
#   partial points will be given if there are small errors.                   #
#                                                                             #
#   Submit your problem sets by 19 July to Livia via email:                   #
#                                                                             #
#   23110870002@m.fudan.edu.cn                                                #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    1. Read in the data in 'wildlife_strikes_CA.xlsx'. Don't forget to       #
#    import pandas.                                                           #
#                                                                             #
###############################################################################

import pandas as pd

wildlife_strikes_CA = pd.read_excel('wildlife_strikes_CA.xlsx')

###############################################################################
#                                                                             #
#    2. Print out the first and last 5 rows. (2 points, freebie)              #
#                                                                             #
###############################################################################

# The `head()` function to view the first five rows.
print(wildlife_strikes_CA.head())

# The `tail()` function to view the last five rows.
print(wildlife_strikes_CA.tail())

###############################################################################
#                                                                             #
#    3. Print out the number of rows and columns in the data. (3 points)      #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    4. Print out the first ten column names. Use the `columns` attribute of  #
#    your dataframe and slice the first ten items. (2 points)                 #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    5. Create a new dataframe under the name `simple_df` that only includes  #
#    the columns 'INCIDENT_DATE', 'AIRPORT_ID', 'SPECIES', 'HEIGHT', 'SPEED', #
#    and 'DISTANCE' (3 points)                                                #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    6. Check for missing values in the 'INCIDENT_DATE', 'AIRPORT_ID', and    #
#    'SPECIES' columns. How many missing values are there in each column?     #
#    (6 points)                                                               #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    7. Write code to reassign `simple_df` to a new dataframe that only       #
#    includes rows where 'INCIDENT_DATE', 'AIRPORT_ID', and 'SPECIES' are not #
#    null. (4 points)                                                         #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    8. Create a new dataframe under the name `pelican_df` where SPECIES is   #
#    'Brown pelican'. How many stikes involved brown pelicans? How many of    #
#    these happened in Los Angeles Intl Airport (AIRPORT_ID="KLAX")?          #
#    (8 points)                                                               #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    9. Let's look into 'HEIGHT,' 'SPEED,' and 'DISTANCE.' Use                #
#    `simple_df.describe().` What did you learn about the speed, altitude,    #
#    and distance from the origin of typical wildlife strikes? (4 points)     #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    10. Create a subset of the data assigned to the variable name            #
#    `strikes_KSFO' Create a new dataframe that includes only data from San   #
#    Francisco International Airport. Use the `describe()` method again to    #
#    compare these statistics with the overall database. (4 points)           #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    11. Save the subsetted KSFO data to a csv and read it back. Use          #
#    `to_csv()` to save your dataframe to a CSV file, and `read_csv()`        #
#    to read it back. (6 points)                                              #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    12. The 'SPECIES' column is a bit messy because it is manually inputted  #
#    by airport personnel and airline staff. Normally to clean messy data,    #
#    you need to manually inspect the data to see what is wrong. We can       #
#    inspect the data more easily first in Excel or Numbers. Use the `Filter' #
#    function in Excel or Numbers to search for these references. Using a     #
#    dictionary, create a mapping of the following groupings of birds:        #
#    'geese,' 'hawks,' and 'gulls' to the messy values you find in your       #
#    manual search. I've added geese, fill the rest in and apply the mapping  #
#    (4 points).                                                              #
#                                                                             #
###############################################################################

species_mapping = {
   'geese' : [
      "Canada goose",
      "Cackling goose",
      "Greater white-fronted goose",
      "Ducks, geese, swans",
      "Geese",
      "Snow goose/Ross's goose complex",
      "Egyptian goose"
   ]
}

###############################################################################
#                                                                             #
#    13. Apply this mapping to your data to create a new column               #
#    `SPECIES_GROUP` and use it to replace the messy data in 'SPECIES'. This  #
#    prepares the dataset for aggregation by cleaner and more consistent      #
#    categories. (8 points)                                                   #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    14. Group by `SPECIES_GROUP` and calculate the number of strikes for     #
#    each species group. (4 points)                                           #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    15. Can you think of regular expressions that would have matched the     #
#    values in your mapping dictionary? As these are human-inputted, this     #
#    might be a more robust way of cleaning the data in case a new variation  #
#    entry appears in the future. Use Python's `re` library to craft three    #
#    regex patterns that could dynamically identify each species group.       #
#    (8 points)                                                               #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    16. Think of an interesting question you can answer with these           #
#    data. Write out that question in 1-2 sentences. Write some code to see   #
#    what you can learn about this question from trends in the data. What did #
#    you find (write another 3-5 sentences)?                                  #
#    (15 points)                                                              #
#                                                                             #
###############################################################################
