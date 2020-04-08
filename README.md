Job Hunter

Created by Dharak Vasavda (d_vasavda@u.pacific.edu) and Nathan Luu (n_luu1@u.pacific.edu)


Aggregating multiple job hunting websites into one. Taking job hunting websites such as indeed.com, and placing it into one universal search engine.

This project will use:

- React (Javascript Framework) as the end-user interaction
- MSSQL Server as the database storage of job information
- (Possibly) CSV for result storage of job information
- Python will scrape the webpages and write out all data to the chosen storage solution


Resources used in project:

https://github.com/ozgur/python-linkedin

https://www.scrapehero.com/tutorial-scraping-linkedin-for-public-company-data/

https://github.com/ozgur/python-linkedin


https://www.codediesel.com/data/quick-way-to-display-csv-files-as-html-tables/


## Understanding the file structure:

indeed.com - contains all web scraping and scraped data for indeed.com

    > indeed.py - handles the scraping
    > jobs.csv - contains all scraped data for indeed.com