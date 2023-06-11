# myjobviz  

![Build status of workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/scrape.yml/badge.svg) ![job-count-1](https://img.shields.io/badge/Total%20jobs%20scraped-1-orange) ![Badge for test workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/test.yml/badge.svg)

Visualize the latest job trends in the IT job market in Mauritius. 

![GIF of visualised data](archive/website-v1.gif)

[▶ Live preview](https://creme332.github.io/mauritius-tech-job-statistics/dist/)

# How it works
1. A selenium web scraper fetches new jobs from myjob.mu on a daily basis.
2. Scraped data is processed and saved to Firestore database.
3. `myjobviz` website fetches processed data from Firestore and creates charts.
# Usage

View instructions on how to setup the project locally [here](docs/setup.md).

# To-do 
* [ ] All x_count functions are duplicates
* [ ] Set merge true when updating
* [ ] Use test data in tests
* [ ] Create choropleth map
* [ ] Add project maintenance in github

* [ ] non-disclosed and negotiable salaries should be valid
* [ ] possible bug with react: you need to react quick
* [ ] add type hinting in each anaylyser files 
* [ ] reinforce tests
* [ ] Add statistics about job title. (for example : count most common jobs)
* [ ] Automatically check for duplicates.
* [ ] Frontend
  + [ ] Add a choropleth map
  + [ ] Add offline support: https://firebase.google.com/docs/firestore/manage-data/enable-offline#web-modular-api
* [ ] Use typescript on frontend
* [ ] Generate charts on backend

## Statistics

Stat  | Data needed | Available
--|--|--
Total jobs scraped | Number of documents in job collection| ✅
Last update of website | Timestamp of last document inserted| ✅
Number of jobs scraped current month | Count of all documents posted in current month| ❌
Number of jobs scraped current month last year | Count of all documents posted in last year| ❌
Number of jobs disclosing salary| Count of all documents posted in last year| ❌
Variation of job count with time| | ❌
Most common job titles| | ❌
Least common job titles (AI, game dev)| | ❌
Relationship between job count and district| | ✅
Frequency of cloud platforms | |✅
Frequency of databases | |✅
Frequency of programming languages| |✅
Frequency of libraries| |✅
Frequency of operating systems| |✅
Frequency of salary| |✅
Frequency of tools| |✅
Frequency of web frameworks| |✅

## After deploying

* [ ] Update service account key on Github
* [ ] Update github workflows
* [ ] update requirements.txt
* [ ] Update repo tags
* [ ] Disable github pages
* [ ] Generate charts on backend
* [ ] Use typescript on frontend
* [ ] update structure of scraped data in readme
# Release notes

## Changes

* Repository name changed from `mauritius-tech-job-statistics` to `myjobviz`.
* A complete rewrite of the the previous code.
  + Restructured entire project
  + Added type checking and docstrings to python code
  + Reduced dependencies in backend (removed bs4)
  + Improved tests
* Project requires two databases instead of one.
* New responsive website with interactive charts.
* New charts(timeseries, boxplot) and more data analysis (job titles, 
* Backup - data scraped is backed up to Google Drive in csv/json format automatically every month
