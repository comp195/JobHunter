Job Hunter

Created by Dharak Vasavda (d_vasavda@u.pacific.edu) and Nathan Luu (n_luu1@u.pacific.edu)


Aggregating multiple job hunting websites into one. Taking job hunting websites such as LinkedIn and Indeed.com, and placing it into one universal search engine.

This project will use:

- React (Javascript Framework) as the end-user interaction
- MSSQL Server as the database storage for job information
- Python will interact with the APIs on the job hunting website to gather the right data


Resources used in project:
https://github.com/ozgur/python-linkedin


## Understanding the file structure:

linkedin.py - web scraper for LinkedIn which will acquire profile data. An account owned by the project owners will be used to request login.
linkedin_data.json - organizes the scraped web data into this json file