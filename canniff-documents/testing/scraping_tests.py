#!/usr/bin/python3.7

'''
Testing the following edge cases:

location = a-z
location = 0-9
location = special chars?
location = doesn't exist?
location = blank
search = a-z
search = 0-9
search = special chars?
search = doesn't exist?
search = blank

'''

import os
import os.path as path
import subprocess


two_dir_up = path.abspath(path.join(__file__ ,"../../.."))
scrape_all_location = two_dir_up + '/scrape_all.py'

# Add quotes to the string
quotes = '"'

###### BEGIN TESTS #######


search_term = "computer science"
location = "san jose"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

########################

search_term = "computer science"
location = "*&$"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

#######################

search_term = "computer science"
location = "san jjjjjjjoooo"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

########################

search_term = "computer science"
location = " "
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

#######################

search_term = "computer science"
location = "san jose"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

########################

search_term = "2817389"
location = "95050"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

#######################

search_term = "computer ^&*@"
location = "san jose"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))

########################

search_term = "sdfd sdjklsjf"
location = "95050"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))


########################

search_term = " "
location = "95050"
os.system('{} {} {} {} {} {} {} {} {} {} {}'.format('python3', scrape_all_location, ' --searchterm ', " ", quotes, search_term, quotes, ' --location ', quotes, location, quotes))