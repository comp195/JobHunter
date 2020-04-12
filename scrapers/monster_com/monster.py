"""
Template source: https://github.com/charissayj/Job-Scraper/blob/master/jobs.py

Usage: python3 monster.py

Functionality: When python file is ran, it updates jobs.csv with the latest search results
"""


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os.path as path
import re
import ssl
import requests
import lxml
import csv


##################################
# Search helper
##################################
# TODO: change search and location to command line arguments
# Searches which the user will interact with
search = 'Computer science'
location = '95050'

# Replace spaces with -
parsed_search = search.replace(' ', '-')
parsed_location = location.replace(' ', '-')

# Give scraper URL to work with
# original URL Example:
#   jobs_url = 'https://www.monster.com/jobs/search/?q=Computer-science&where=bay-area'

jobs_url = ('https://www.monster.com/jobs/search/?q=' + parsed_search + '&l=' + parsed_location)


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
