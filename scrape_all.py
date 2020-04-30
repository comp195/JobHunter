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

import os
import subprocess
import argparse
import random
import csv

# Get command line arguments
parser = argparse.ArgumentParser(description='Scrape from all data sources and update their .csv files.\n')
parser.add_argument("--searchterm", default=None, type=str, required=True, help="The job search term, such as Biology or Computer Science. Place in quotes")
parser.add_argument("--location", default=None, type=str, required=True, help="Specify the job search's location. It can be a string as a city and/or state (San jose, CA) or a zip code (95050). Place in quotes")


# Command line arguments are placed into variables and these will act as the job search term
# These will be concatenated into the scraper command line arguments to scrape data for that search
args = parser.parse_args()
search_term = args.searchterm
location = args.location


# Initialize path for scrapers
# Get current working directory
cwd = os.path.dirname(os.path.realpath(__file__))
indeed_path = (cwd + '/scrapers/indeed_com/indeed.py')
monster_path = (cwd + '/scrapers/monster_com/monster.py')
indeed_csv_path = (cwd + '/front-end/src/csv/indeed_jobs.csv')
monster_csv_path = (cwd + '/front-end/src/csv/monster_jobs.csv')
allJobs_csv_path = (cwd + '/front-end/src/csv/allJobs.csv') # Where both .csv files will be combined


# Gain elevated user permissions to call files
subprocess.Popen('chmod +x ' + indeed_path, shell=True)
subprocess.Popen('chmod +x ' + monster_path, shell=True)

print('Scraping all data now...\n')


# Add quotes to the string
quotes = '"'


# Run shell prompt to run the python files
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', indeed_path, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))
print('\n')

os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', monster_path, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))
print('\n')


# Combine both jobs.csv files
print('Combining both jobs.csv files now...\n')

reader = csv.reader(open(indeed_csv_path))
reader1 = csv.reader(open(monster_csv_path))
f = open(allJobs_csv_path, "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)
for row in reader1:
    writer.writerow(row)

f.close()


# Randomize both CSV files' lines
print('Randomizing lines of jobs.csv now...\n')

with open(allJobs_csv_path,'r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open(allJobs_csv_path,'w') as target:
    for _, line in data:
        target.write( line )


# Re-write header to randomize
header = "Title,Company,Location,Link,JobSource\n"

with open(allJobs_csv_path) as f:
    lines = f.readlines() #read

lines[0] = header # Write to line 1

with open(allJobs_csv_path, "w") as f:
    f.writelines(lines) # Write back