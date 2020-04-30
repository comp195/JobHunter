# Job Hunter

Aggregating multiple job hunting websites into one. Taking job hunting websites indeed.com and monster.com and placing it into one universal search engine.

Created by Dharak Vasavda (d_vasavda@u.pacific.edu) and Nathan Luu (n_luu1@u.pacific.edu)

# Link to App Website:
https://bit.ly/2VQZzfC

#

## Project Technologies Used? Purposes?

- React (Javascript Framework) as the end-user interaction
- Neflify for website hosting
- CSV for scraped job information storage
- Python will scrape the webpages and write out all data to the chosen storage solution


# Q and A:

## How to Scrape All Job Data?

1. Go to the root of the project dir
2. Run the example command:
    `python3 scrape_all.py --searchterm "computer science" --location '95050'`


## Where is all of the Scraped Job Data scored?
All job data can be found under `/front-end/src/csv/`


## What happens with the scraped job data?
All of the scraped job data will be placed into its respective `jobs.csv` file. From there, React framework will parse the lines of data in `jobs.csv` and display the results in its own webpage interface.


## How is the Website Hosted?
Using a service called `Netlify`. Whenever new code is pushed to this repository on branch `master`, Netlify (https://www.netlify.com) will build a new version of the website. Netlify uses CI/CD to detect updates to the branch and will automatically update the webpage.


## Is the website Static or Dynamic? Is the data live or static?
- The website is Static. Hosting a dynamic website with React will run the project into using paid web hosting services which is out of the scope for this. This project runs as a proof-of-concept that multiple job hunting websites can be aggregated into one. As a side note, the service can be created into a dynamic one as the code is fully prepared for it.
- The data is static. It is scraped once per push to the repository and is then displayed onto the website. To enable live scraping, the repository would need to be hosted on a server which allows a database instance.


## What language is the website built in?
React, a JavaScript library (https://reactjs.org)


## How do I access the website to test this app?
Link is above under "Link to App Website" as well:  https://bit.ly/2VQZzfC




### Resources used in project:

https://www.codediesel.com/data/quick-way-to-display-csv-files-as-html-tables/

https://ermir.net/topic-15/web-scraping-indeed-and-monster-job-portals-using-python
