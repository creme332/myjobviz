# myjobviz  
![Build status of workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/scrape.yml/badge.svg)
![Badge storing the total number of jobs scraped](https://img.shields.io/badge/myjobviz-v3-orange)
![Badge for test workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/test.yml/badge.svg)

Visualize the latest job trends in the IT job market in Mauritius. 

![GIF of visualised data](website.gif)

[▶ Live preview](https://creme332.github.io/mauritius-tech-job-statistics/dist/)

# How it works
1. A selenium web scraper fetches new jobs from myjob.mu on a daily basis.
2. Scraped data is processed and saved to Firestore.
3. `myjobviz` website fetches processed data from Firestore and creates charts.

# Tools used
Python is used for scraping and managing the database.

## frontend
- React
- 
# Usage
View instructions on how to setup the project locally [here](docs/setup.md).


# To-do 
- [ ] Generate new service account key
- [ ] Setup typescript for frontend
- [ ] Paste package.json



- [ ] In `analyser` folder, make it easier to add/remove techs. Also make use of dictUtils.
- [ ] Automatically check for duplicates.
- [ ] update structure of scraped data in readme
- [ ] Add timeseries data viz.
- [ ] Add tests for scraper.
- [ ] Add try catch in scraper
- [ ] Add a workflow to backup database (and maybe release a public version).
- [ ] Fix : Riviere du Rempart district includes some nearby small islands.
- [ ] Add statistics about job title. (for example : count most common jobs)
- [ ] Use unique colours in salary chart.
- [ ] Improve UI of website.

## After deploying
- [ ] Update service account key on Github
