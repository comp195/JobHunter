# Template source: https://github.com/charissayj/Job-Scraper/blob/master/jobs.py

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import ssl


# Searches which the user will interact with
search = 'Computer science'
location = 'San Jose'

# Split the string into usable
parsed_search = ''
parsed_location = ''

# Give scraper URL to work with
jobs_url = 'https://www.indeed.com/jobs?q=computer+science&l=95050'



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

headers = "Title, Company, Location, Experience, Link \n"

f.write(headers)



# Data Scraping
for i in results:
    job_title = i.find('a', {'data-tn-element': 'jobTitle'})['title']
    company_name = i.find('span', {'class': 'company'}).text.strip()
    job_summary = ''.join([j.text.strip() for j in i.find_all('span',
                                                            {'class': 'summary'})])

    location = i.find('span', {'class': 'location'})
    if location is not None:
        location = location.text.strip()

    salary_range = i.find('span', {'class': 'no-wrap'})
    if salary_range is not None:
        salary_range = salary_range.text.strip()

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
    f.write(job_summary + ', ')
    # f.write(location + '\n')
    f.write('\n')

f.close()
