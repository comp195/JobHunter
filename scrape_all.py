#!/usr/bin/python3.7

'''
Run this file to gather all scraping results for
- indeed.com
- monster.com

Usage:
    python3 scrape_all.py <"job search term"> <"location">
    (quotes are required)

Example:
    python3 scrape_all.py --searchterm "computer science" --location 'san jose'

Where:
    <location> can be a string as a city and/or state (San jose, CA) or an int as a zip code (95050)
'''

from scrapers.indeed_com import indeed
from scrapers.monster_com import monster
import os
import subprocess
import argparse


# Get command line arguments
parser = argparse.ArgumentParser(description='Scrape from all data sources and update their .csv files.\n')
parser.add_argument("--searchterm", default=None, type=str, required=True, help="The job search term, such as Biology or Computer Science. Place in quotes")
parser.add_argument("--location", default=None, type=str, required=True, help="Specify the job search's location. It can be a string as a city and/or state (San jose, CA) or a zip code (95050). Place in quotes")


# Command line arguments are placed into variables and these will act as the job search term
# These will be concatenated into the scraper command line arguments to scrape data for that search
args = parser.parse_args()
search_term = args.searchterm
location = args.location

print(search_term)
print(location)


# Initialize path for scrapers
# Get current working directory
cwd = os.path.dirname(os.path.realpath(__file__))
indeed_path = (cwd + '/scrapers/indeed_com/indeed.py')
monster_path = (cwd + '/scrapers/monster_com/monster.py')

# Gain elevated user permissions to call files
subprocess.Popen('chmod +x ' + indeed_path, shell=True)
subprocess.Popen('chmod +x ' + monster_path, shell=True)

print('Scraping all data now...\n')

# Run shell prompt to run the python files
os.system('{} {}'.format('python3', indeed_path))
print('\n')
os.system('{} {}'.format('python3', monster_path))
print('\n')