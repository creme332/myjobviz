# mauritius-tech-job-scraper 📊 
![Build status of workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/scrape.yml/badge.svg)
![Badge storing the total number of jobs scraped](https://img.shields.io/badge/Total%20jobs%20scraped-366-orange)

An automatic web scraper which scrapes IT jobs from [`myjob.mu`](myjob.mu) using Github Actions and Selenium. Scraped data is saved to Google Firestore and data visualisations are deployed on Github Pages. 

[▶ Live preview](https://github.com/creme332/mauritius-tech-job-statistics/dist)

# To-do 
- [ ] In `analyser` folder, make it easier to add/remove techs. Also make use of dictUtils.
- [ ] Automatically check for duplicates.
- [ ] update structure of scraped data in readme
- [ ] Add timeseries data viz
- [ ] add a workflow to backup database (and maybe release a public version)
- [ ] Fix : Riviere du Rempart district includes some nearby small islands.
- [ ] add statistics about job title. (for example : count most common jobs)
  
# Features
- Automatic scraping every day using Github Actions.
- Scraped data is saved to a Google Firestore database.
- Wide range of plots (pie chart, donut chart, choropleth map, lollipop chart, ... ).
- Responsive website.

# Installation
Clone project
```
git clone git@github.com:creme332/mauritius-tech-job-statistics.git
```
Install dependencies for website:
```
npm install
```
Install dependencies for scraper:
```
pip install
```
## Setting up Firestore database 
[Create a Firestore database](https://firebase.google.com/docs/firestore/quickstart#create) and generate a service account key in JSON format.

Convert your service account key JSON to a base-64 encoded string by running the following code:
```python
import json
import base64

# replace JSON below with yours
service_key = {
    "type": "service_account",
    "project_id": "xxx",
    "private_key_id": "xxx",
    "private_key": "-----BEGIN PRIVATE KEY-----\nxxxxx\n-----END PRIVATE KEY-----\n",
    "client_email": "xxxx.com",
    "client_id": "xxxx",
    "auth_uri": "xxxx",
    "token_uri": "xxxx",
    "auth_provider_x509_cert_url": "xxxx",
    "client_x509_cert_url": "xxxx"
}

# convert json to a string
service_key = json.dumps(service_key)

# encode service key
encoded_service_key= base64.b64encode(service_key.encode('utf-8'))

print(encoded_service_key)
# FORMAT: b'a_lot_of_chars'
```

Create `.env` file in the root directory of the project and add following:
```js
SERVICE_ACCOUNT_KEY = b'a_lot_of_chars'
```

Create a Github Secret `SERVICE_ACCOUNT_KEY` with value given by `encoded_service_key`.

Initialise documents in Firestore by running the following code in `miner.py` :
```python
from classes.database import Database

my_database = Database()
my_database.initialise_stats_collection()
```
Restore `miner.py` to its initial state afterwards.

## Testing
Run python tests in the root directory of the project:
```
nose2
```

## Scraping

Run program in terminal (or otherwise):
```sh
python src/main.py
```
> Scraping the website and analysing the data for the first time will take around 40 minutes. You can temporarily set  `self.crawl_delay = 2` in `miner.py` to speed up the process.

### Structure of scraped data ##
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
- `date_posted` and `closing_date` are strings which follow `DD/MM/YYYY` format.

# Attributions

Resource | Source | Note
---|---| ---|
[Geojson file for Mauritian districts](data/mauritius-districts-geojson.json) | https://data.govmu.org/dkan/?q=dataset/mauritius-districts | The original geojson file contains some spelling mistakes which were corrected in [my version of the geojson file](data/mauritius-districts-geojson.json).
