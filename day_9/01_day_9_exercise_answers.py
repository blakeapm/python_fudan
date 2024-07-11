###############################################################################
#                                                                             #
#    1. Import the regex package `re`, define file paths.                     #
#                                                                             #
###############################################################################

import re

'''
You will want to add the path here to your day_9 folder on your computer
To access this, navigate to the day_9 folder in the shell with the command `cd`
and print the working directory with the command `pwd` paste the output in
place of '/Users/your_username/Documents/python_fudan/day_9'
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

locations = []
with open(working_dir + '/' + input_fn, 'r') as f:
    for line in f:
        word = line.strip()
        locations.append(word)

###############################################################################
#                                                                             #
#    3. Write regular expressions for each state.                             #
#                                                                             #
###############################################################################

ca_pattern = r'\bC\w+\b\.?'
wa_pattern = r'\bW\w+\b\.?'
ma_pattern = r'\bM\w+\b\.?'

###############################################################################
#                                                                             #
#    4. Define a function to standardize the state names using your regex.    #
#                                                                             #
###############################################################################

def standardize_state_name(location):
    location = re.sub(ca_pattern, 'CA', location)
    location = re.sub(wa_pattern, 'WA', location)
    location = re.sub(ma_pattern, 'MA', location)
    return location

###############################################################################
#                                                                             #
#    5. Apply the standardization function to each location using a loop.     #
#                                                                             #
###############################################################################

standardized_locations = []
for location in locations:
    standardized_location = standardize_state_name(location)
    standardized_locations.append(standardized_location)

###############################################################################
#                                                                             #
#    6. Write the standardized locations to output_file_path                  #
#    ('twitter_locations_clean.txt').                                         #
#                                                                             #
###############################################################################

with open(output_fn, 'w') as f:
    for location in standardized_locations:
        f.write(location + '\n')

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

def standardize_state_name(location):
    if location.startswith('C'):
        return 'California'
    elif location.startswith('W'):
        return 'Washington'
    elif location.startswith('M'):
        return 'Massachusetts'
    return None

###############################################################################
#                                                                             #
#    8. Now read in the `twitter_data.csv` file as a DataFrame in Pandas      #
#    Print our the first and last 10 rows of the data frame.                  #
#                                                                             #
###############################################################################

import pandas as pd


twitter_data = pd.read_csv(working_dir + '/' + input_csv_fn, index=False)

twitter_data.head(10)
twitter_data.tail(10)
