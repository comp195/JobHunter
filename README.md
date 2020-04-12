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

https://ermir.net/topic-15/web-scraping-indeed-and-monster-job-portals-using-python


## How to Scrape All Job Data

1. Go to the root of the project dir
2. Run the example command:
    `python3 scrape_all.py --searchterm "computer science" --location '95050'`


## Where is all of the Scraped Job Data?
For `indeed.com`:

All job data is contained in `/scrapers/indeed_com/jobs.csv`

For `indeed.com`:

All job data is contained in `/scrapers/monster_com/jobs.csv`

## What happens with the scraped job data?
All of the scraped job data will be placed into its respective `jobs.csv` file. From there, React framework will parse the lines of data in `jobs.csv` and display the results in its own webpage interface.