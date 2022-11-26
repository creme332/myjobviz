# mauritius-tech-job-scraper 📊 
![Build status of workflow](https://github.com/creme332/mauritius-scholarship-alert/actions/workflows/main.yml/badge.svg)

An automatic web scraper which scrapes IT jobs from `myjob.mu` using Github Actions and Selenium. Scraped data is saved to Google Firestore and data visualisations are deployed on Github Pages. 

# To-do 
- [ ] in analyser functions pass around a single dictionary. make use of dictUtils.
- [ ] update `requirements.txt`.
- [ ] deal with case where collection is empty in library 
- [ ] implement [github scraping workflow](https://github.com/MarketingPipeline/Python-Selenium-Action/blob/main/.github/workflows/Selenium-Action_Template.yaml)
- [ ] Add timeseries data viz
- [ ] add a workflow to backup database (and maybe release a public version)
- [ ] add a badge for number of jobs scraped
- [ ] Fix : Riviere du Rempart district includes some nearby small islands.

- [x] Work on website
- [x] save new jobs just after scraping
- [x] find a way to run all tests at once
- [x] add docstrings to all functions
- [x] use a cumulative approach : instead of having to analyse whole database every time, analyse only new jobs.
- [x] add tests for `analyser.py`
- [x] breakdown `analyser.py` in smaller modules.
- [x] store database size, 
- [x] fetch only 200 most recent jobs.	
- [x] change data type of `date_posted` and `closing_date` to date in firestore
- [x] add progress bar in miner
- [x] save library to cloud firestore
- [x] try to request a second time without sleeping
- [x] update analyser and visualiser. 

## statistics
- [ ] add statistics for each job title.
  
# Features
- Automatic scraping every day using Github Actions.
- Scraped data is saved to a Google Firestore database.
- Wide range of plots (pie chart, donut chart, choropleth map, lollipop chart, ... ).
- Responsive website.

## Structure of scraped data ##
```
{
	'job_title': 'télévendeurs avec expérience (1 an minimum)',
	'date_posted': '31/10/2022',
	'closing_date': '30/11/2022',
	'url': 'http://myjob.mu/Jobs/TELEVENDEURS-AVEC-EXPERIENCE-1-AN-135694.aspx',
	'location': '\nMoka ',
	'employment_type': 'Permanent',
	'company': 'EURO CRM (Mauritius) Ltd',
	'salary': '10,000 - 20,000',
	'job_details': "\nLe Télévendeur prospecte et ... \n"
}
```

### Notes
- The URLs scraped may not work as myjob.mu takes down a job post after a certain time. 
- The job URL was used as a primary key during scraping to avoid duplicate entries.
- `job_title` and `job_details` can be in French or English. 
- `salary` is not always disclosed.
- `date_posted` and `closing_date` are strings which follow `DD/MM/YYYY` format.

# Attributions

Resource | Source | Note
---|---| ---|
[Geojson file for Mauritian districts](data/mauritius-districts-geojson.json) | https://data.govmu.org/dkan/?q=dataset/mauritius-districts | The original geojson file contains some spelling mistakes which were corrected in [my version of the geojson file](data/mauritius-districts-geojson.json) .

# Installation
```
git clone
```
Install dependencies for website:
```
npm install
```
Install dependencies for scraper:
```
pip install
```

Create a firestore database and get a service account key for this database.

Create `.env` file at the root directory with details from the service account key:
```js
TYPE = "service_account"
PROJECT_ID = "XXXX"
PRIVATE_KEY_ID = "XXXX"
PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----XXXX-----END PRIVATE KEY-----\n"
CLIENT_EMAIL = "XXXX"
CLIENT_ID = "XXXX"
AUTH_URI = "XXXX"
TOKEN_URI = "XXXX"
AUTH_PROVIDER_X509_CERT_URL = "XXXX"
CLIENT_X509_CERT_URL = "XXXX"
```

Run python tests in the root directory of the project:
```
nose2
```