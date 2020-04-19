"""
Template source: https://github.com/charissayj/Job-Scraper/blob/master/jobs.py

Usage:
    python3 monster.py --searchterm "search" --location "location"

Example:
    python3 monster.py --searchterm "computer science" --location "san jose"

Functionality:
    When python file is ran, it updates jobs.csv with the latest search results
"""


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os.path as path
import re
import ssl
import requests
import lxml
import csv
import argparse


##################################
# Command line args helper
##################################
# Get command line arguments
parser = argparse.ArgumentParser(description='Scrape from indeed.com\n')
parser.add_argument("--searchterm", default=None, type=str, required=True, help="The job search term, such as Biology or Computer Science. Place in quotes")
parser.add_argument("--location", default=None, type=str, required=True, help="Specify the job search's location. It can be a string as a city and/or state (San jose, CA) or a zip code (95050). Place in quotes")


# Command line arguments are placed into variables and these will act as the job search term
# These will be concatenated into the scraper command line arguments to scrape data for that search
args = parser.parse_args()
search_term = args.searchterm
location = args.location





##################################
# Search helper
##################################
# Searches which the user will interact with
# search = 'Computer science'
# location = '95050'

# Replace spaces with -
parsed_search = search_term.replace(' ', '-')
parsed_location = location.replace(' ', '-')
parsed_location = parsed_location.replace(',', '__2C')


# Give scraper URL to work with
# original URL Example:
#   jobs_url = 'https://www.monster.com/jobs/search/?q=computer-science&where=san-diego'

jobs_url = ('https://www.monster.com/jobs/search/?q=' + parsed_search + '&where=' + parsed_location)


print('Scraping data from Monster.com URL: ' + jobs_url)





##################################
# Data and web connectors
##################################
# opening connection and grabbing the page
uClient = uReq(jobs_url)
page_html = uClient.read()
uClient.close()

# html parsing
soup = soup(page_html, 'html.parser')

# grab all divs with a class of row
jobs_container = soup.find(id='ResultsContainer')

job_items = jobs_container.find_all('section', class_='card-content')

# print(len(results))

# Need to specify absolute path to work with scrape_all.py
two_dir_up = path.abspath(path.join(__file__ ,"../.."))
filename = two_dir_up + '/monster_com/jobs.csv'
f = open(filename, "w")

headers = "Title | Company | Location | Link \n"

f.write(headers)

# all_jobs = []





##################################
# Web Scraping and file writeout
##################################
for i in job_items:

    # company_name = i.find('span', {'class': 'company'}).text.strip()
    title_elem = i.find('h2', class_='title')
    company_elem = i.find('div', class_='company')
    location_elem = i.find('div', class_='location')
    url_elem = i.find('a')


    if None in (title_elem, company_elem, url_elem):
        continue

    # get the full url of this listing
    href = url_elem.get('href')
    if href is None:
        continue

    item = {
        "Title" : title_elem.text.strip(),
        "Company" : company_elem.text.strip(),
        "Location" : location_elem.text.strip(),
        "Link" : href,
        # "description" : "",
        # "description_text" : ""
    }

    # Optional: Write all jobs to an array
    # all_jobs.append(item)


    # Output all data to jobs.csv
    f.write(item.get("Title", "") + ' | ')
    f.write(item.get("Company", "") + ' | ')
    f.write(item.get("Location", "") + ' | ')
    f.write(item.get("Link", ""))
    f.write('\n')


print('monster.com - Finished scraping data. Results were placed in /scrapers/monster.com/jobs.csv')

f.close()
