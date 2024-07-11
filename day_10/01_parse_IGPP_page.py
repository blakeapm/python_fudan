import os
import pandas as pd
import re
import requests
    
from bs4 import BeautifulSoup

# Helper function to extract next sibling text
def sibling_text(tag):
    span_tag = tag.next_sibling.text
    return span_tag.lstrip(': ').strip()

def get_url_source(url):
    # Make the request to get the page content
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.content

# Set the base directory to save the file in
#base_dir = '/Users/your-user-name/Documents/python_fudan/'
base_dir = '/Users/lcl-admin/Documents/python_fudan/day_10/'

# Check if we've scraped it already
if not os.path.isfile(base_dir + 'course_overview_fudan.html'):
    # Download the source code for the course info page
    url = "https://igpp.fudan.edu.cn/summer_school_en/kcjj/list.htm"
    content = get_url_source(url)
    # Write the HTML content
    with open(base_dir + 'course_overview_fudan.html', 'w') as f:
        f.write(content)
else:
    # Load the HTML content
    with open(base_dir + 'course_overview_fudan.html', 'r') as f:
        content = f.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all the divs with the class 'page-right-card-item'
divs = soup.find_all('div', class_='page-right-card-item')

# Initialize the list to hold the dictionaries for each course
rows = []

# Iterate through each course div
for div in divs:
    row = {}
    
    # Extract the title
    title_tag = div.find('div', class_='page-right-card-item-title').find('a')
    title = title_tag.text.strip() if title_tag else ''

    # Extract the title and affiliation
    title_affiliation_tag = div.find('span', string='Title and Affiliation')
    title_affiliation = sibling_text(title_affiliation_tag)
    title_affiliation = title_affiliation.split(', ')
    if len(title_affiliation) == 1:
        title_affiliation = title_affiliation[0].split('，')

    title, affiliation = title_affiliation

    # Extract the time and session number
    time_tag = div.find('span', string='Time')
    time_session = sibling_text(time_tag).split('Session')
    time, session_no = time_session
    session_no = re.search(r'[0-9]', session_no).group()

    # Extract the course description
    description_tag = div.find('div', class_='page-jj').find('span', string='Course Description')
    description = sibling_text(description_tag)

    # Extract the instructor name
    instructor_tag = div.find('span', string='lnstructor Name')
    instructor_name = sibling_text(instructor_tag)
    instructor_names = []
    if '&' in instructor_name:
        instructor_names = [i.split() for i in instructor_name.split(' & ')]
    else:
        instructor_names.append(instructor_name.split())

    # Create a new row for each instructor
    for name in instructor_names:
        # Fits convention for Chinese and English names
        if len(name) <= 3:
            last = name[-1].title()
            first = ' '.join(name[:-1])
        # Fits convention for Spanish/Portuguese names
        else:
            first = ' '.join(name[:2])
            last = ' '.join(name[2:])
        row = {
            'title': title,
            'affiliation': affiliation,
            'time': time,
            'session_no': session_no,
            'course_description': description,
            'instructor_last_name': last,
            'instructor_first_name': first
        }
        rows.append(row)

# Output the data as a csv
courses_df = pd.DataFrame(rows)
courses_df.to_csv(base_dir + 'course_info.csv', index=False)

# Output the list of row dictionaries
courses_df = pd.DataFrame(rows)
courses_df.to_csv(base_dir + 'course_info.csv', index=False)
