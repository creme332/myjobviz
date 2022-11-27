# mauritius-tech-job-scraper 📊 
![Build status of workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/scrape.yml/badge.svg)
![Badge storing the total number of jobs scraped](https://img.shields.io/badge/Total%20jobs%20scraped-100-brightgreen)

An automatic web scraper which scrapes IT jobs from `myjob.mu` using Github Actions and Selenium. Scraped data is saved to Google Firestore and data visualisations are deployed on Github Pages. 

[▶ Live preview](https://github.com/creme332/mauritius-tech-job-statistics/dist)

# To-do 
- [ ] in analyser functions pass around a single dictionary. make use of dictUtils.
- [ ] automatically check for duplicates.
- [ ] find new method to identify duplicates.
- [ ] add a server timestamp to each job
- [ ] add a workflow to run tests.
- [ ] deal with case where collection is empty in library 
- [ ] Add timeseries data viz
- [ ] add a workflow to backup database (and maybe release a public version)
- [ ] add a badge for number of jobs scraped
- [ ] Fix : Riviere du Rempart district includes some nearby small islands.
- [ ] add statistics about job title. (for example : count most common jobs)
  
# Features
- Automatic scraping every day using Github Actions.
- Scraped data is saved to a Google Firestore database.
- Wide range of plots (pie chart, donut chart, choropleth map, lollipop chart, ... ).
- Responsive website.

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

Create a firestore database and get a service account key.

Create `.env` file at the root directory with details from the service account key:
```js
SERVICE_ACCOUNT_KEY = b'a_lot_of_chars'

```

Run python tests in the root directory of the project:
```
nose2
```

To scrape website for the first time:

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
[Geojson file for Mauritian districts](data/mauritius-districts-geojson.json) | https://data.govmu.org/dkan/?q=dataset/mauritius-districts | The original geojson file contains some spelling mistakes which were corrected in [my version of the geojson file](data/mauritius-districts-geojson.json).
