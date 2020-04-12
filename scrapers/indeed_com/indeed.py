"""
Template source: https://github.com/charissayj/Job-Scraper/blob/master/jobs.py

Usage:
    python3 indeed.py --searchterm "search" --location "location"

Example:
    python3 indeed.py --searchterm "computer science" --location "san jose"

Functionality:
    When python file is ran, it updates jobs.csv with the latest search results
"""


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import os.path as path
import re
import ssl
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
# TODO: change search and location to command line arguments
# Searches which the user will interact with
# search = 'Computer science'
# location = '95050'

# Replace spaces with +
parsed_search = search_term.replace(' ', '+')
parsed_location = location.replace(' ', '+')

# Give scraper URL to work with
# original URL Example:
#   jobs_url = 'https://www.indeed.com/jobs?q=computer+science&l=san+jose'

jobs_url = ('https://www.indeed.com/jobs?q=' + parsed_search + '&l=' + parsed_location)


print('Scraping data from Indeed.com URL: ' + jobs_url)





##################################
# Data and web connectors
##################################
# opening connection and grabbing the page
uClient = uReq(jobs_url)
page_html = uClient.read()
uClient.close()

# html parsing
soup = soup(page_html, "html.parser")

#grab all divs with a class of result
results = soup.find_all('div', {'class': 'result'})

#print len(results)
# Need to specify absolute path to work with scrape_all.py
two_dir_up = path.abspath(path.join(__file__ ,"../.."))
filename = two_dir_up + '/indeed_com/jobs.csv'
f = open(filename, "w")

headers = "Title | Company | Location | Link \n"

f.write(headers)





##################################
# Web Scraping and file writeout
##################################
for i in results:
    # Job Title
    job_title = i.find('a', {'data-tn-element': 'jobTitle'})['title']

    # Company Name
    company_name = i.find('span', {'class': 'company'}).text.strip()

    # Location
    location_search = i.find('div', attrs={'class': 'location accessible-contrast-color-location'})
    if location_search is not None:
            location = location_search.text.strip()


    # Job Link
    url_elem = i.find('a', {'target': '_blank'})

    # get the href of this listing
    # the format will be such as '/pagead/' which will later need to be concatenated
    # with 'indeed.com'
    href = url_elem.get('href')
    if href is None:
        continue

    job_link = 'https://www.indeed.com' + href


    # Optional: write all data out to an array
    # data = []

    # # write out to an array
    # datum = {'job_title': job_title,
    #         'company_name': company_name,
    #         'job_summary': job_summary,
    #         'location': location,
    #         'salary_range': salary_range}

    # data.append(datum)

    f.write(job_title + ' | ')
    f.write(company_name + ' | ')
    # f.write(job_summary + ', ')
    f.write(location + ' | ')
    f.write(job_link)
    # f.write(days_ago_posted + ', ')
    f.write('\n')


print('indeed.com - Finished scraping data. Results were placed in /scrapers/indeed.com/jobs.csv')

f.close()
