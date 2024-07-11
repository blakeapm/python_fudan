###############################################################################
#                                                                             #
#    1. Import the regex package `re`, define file paths.                     #
#                                                                             #
###############################################################################

import re

'''
You will want to add the path here to your day_8 folder on your computer
To access this, navigate to the day_8 folder in the shell with the command `cd`
and print the working directory with the command `pwd` paste the output in
place of '/Users/your_username/Documents/python_fudan/day_8'
'''

working_dir = '/Users/your_username/Documents/python_fudan/day_9'

input_csv_fn = 'twitter_data.csv'
input_fn = 'twitter_locations.txt'
output_fn = 'twitter_locations_clean.txt'

###############################################################################
#                                                                             #
#    2. Read in the data from 'twitter_profile_locations.txt' using a loop.   #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    3. Write regular expressions for each state.                             #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    4. Define a function to standardize the state names using your regex.    #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    5. Apply the standardization function to each location using a loop.     #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    6. Write the standardized locations to output_file_path                  #
#    ('twitter_locations_clean.txt').                                         #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    7. Now rewrite standardize_state_name function to use string functions   #
#    instead. Can you produce the same output with .startswith()? See the     #
#    slide from `day_5_slides.pdf` titled:                                    #
#    `String Methods: Finding and Replacing`                                  #
#                                                                             #
#    Change the output_fn variable to `twitter_locations_str.txt`.            #
#    Rerun this code and compare the output to `twitter_locations_clean.txt`  #
#                                                                             #
###############################################################################

###############################################################################
#                                                                             #
#    8. Now read in the `twitter_data.csv` file as a DataFrame in Pandas      #
#    Print our the first and last 10 rows of the data frame.                  #
#                                                                             #
###############################################################################
