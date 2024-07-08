###############################################################################
#                                                                             #
#    1. Import the regex package `re`, define file paths.                     #
#                                                                             #
###############################################################################

import re

'''
You will want to add the path here to your day_5 folder on your computer
To access this, navigate to the day_5 folder in the shell with the command `cd`
and print the working directory with the command `pwd` paste the output in
place of '/Users/your_username/Documents/python_fudan/day_5'
'''

working_dir = '/Users/your_username/Documents/python_fudan/day_5'

input_fn = 'twitter_locations.txt'
output_fn = 'twitter_locations_clean.txt'

###############################################################################
#                                                                             #
#    2. Read in the data from 'twitter_profile_locations.txt' using a loop.   #
#                                                                             #
###############################################################################

locations = []
fin = open(working_dir + '/' + input_fn, 'r')
for line in fin:
    word = line.strip()
    locations.append(word)
fin.close()

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
    location = re.sub(ca_pattern, 'California', location)
    location = re.sub(wa_pattern, 'Washington', location)
    location = re.sub(ma_pattern, 'Massachusetts', location)
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
