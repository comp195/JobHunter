"""
Template source: https://github.com/charissayj/Job-Scraper/blob/master/jobs.py

Usage: python3 indeed.py

Functionality: When python file is ran, it updates jobs.csv with the latest search results
"""


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import ssl



##################################
# Search helper
##################################
# TODO: change search and location to command line arguments
# Searches which the user will interact with
search = 'Computer science'
location = '95050'

# Replace spaces with +
parsed_search = search.replace(' ', '+')
parsed_location = location.replace(' ', '+')

# Give scraper URL to work with
# original URL Example:
#   jobs_url = 'https://www.indeed.com/jobs?q=computer+science&l=san+jose'

jobs_url = ('https://www.indeed.com/jobs?q=' + parsed_search + '&l=' + parsed_location)


print('Scraping data from URL: ' + jobs_url)


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
filename = "jobs.csv"
f = open(filename, "w")

headers = "Title, Company, City, State, Days Ago Posted, Link \n"

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
    # Wrapped within 1 div
    for location_search in soup.find_all('div', attrs={'class': 'sjcl'}):
        location = location_search.find('div', attrs={'class': 'location accessible-contrast-color-location'})
        if location is not None:
            location = location.text.strip()

    # Days Ago posted
    # Wrapped within 4 divs
    # TODO: Speed this up
    # for div1 in soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard-footer'}):
    #     for div2 in soup.find_all('div', attrs={'class': 'jobsearch-SerpJobCard-footerActions'}):
    #         for div3 in soup.find_all('div', attrs={'class': 'result-link-bar-container'}):
    #             for div4 in soup.find_all('div', attrs={'class': 'result-link-bar'}):
    #                 days_ago_posted = div4.find('div', attrs={'class': 'date '})
    #                 if days_ago_posted is not None:
    #                     days_ago_posted = days_ago_posted.text.strip()


    # Link to Job entry
    # link = results.i['href']
    # job_link = ("https://www.indeed.com" + link)



    # Optional: write all data out to an array
    # data = []

    # # write out to an array
    # datum = {'job_title': job_title,
    #         'company_name': company_name,
    #         'job_summary': job_summary,
    #         'location': location,
    #         'salary_range': salary_range}

    # data.append(datum)

    f.write(job_title + ', ')
    f.write(company_name + ', ')
    # f.write(job_summary + ', ')
    f.write(location + ', ')
    # f.write(days_ago_posted + ', ')
    # f.write(job_link + '\n')
    f.write('\n')



f.close()
