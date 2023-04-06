# mauritius-tech-job-scraper 📊 
![Build status of workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/scrape.yml/badge.svg)
![Badge storing the total number of jobs scraped](https://img.shields.io/badge/Total%20jobs%20scraped-1608-orange)
![Badge for test workflow](https://github.com/creme332/mauritius-tech-job-statistics/actions/workflows/test.yml/badge.svg)

An automatic web scraper which scrapes IT jobs from [`myjob.mu`](https://www.myjob.mu/) using Github Actions and Selenium. Scraped data is saved to Google Firestore and data visualisations are deployed on Github Pages. 

![GIF of visualised data](website.gif)

[▶ Live preview](https://creme332.github.io/mauritius-tech-job-statistics/dist/)
  
# Features
- Automatic daily scraping using Github Actions.
- Scraped data is saved to a Google Firestore database.
- Multiple data analysed : salary, common technologies, ...
- Wide range of plots : interactive plots, pie chart, donut chart, choropleth map, lollipop chart, ... 
- Responsive website.

# Installation
Clone project:
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

Convert your service account key JSON to a base-64 encoded string by running the python code below:

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

Create a `.env` file in the root directory and create an environment variable `SERVICE_ACCOUNT_KEY` having the same value as `encoded_service_key`:
```js
SERVICE_ACCOUNT_KEY = b'a_lot_of_chars'
```
> Notice how the value starts with `b'` and ends with `'`. Obey this format.

Create a Github Secret `SERVICE_ACCOUNT_KEY` with value given by `encoded_service_key`.

Initialise your Firestore database by running the following function in `main.py` :
```python
rebaseStatsCollection()
```

# Usage
Run main program in terminal (or otherwise):
```sh
python src/main.py
```
> Scraping the website and analysing the data for the first time will take around 40 minutes. You can temporarily set  `self.crawl_delay = 2` in `miner.py` to speed up the process.

Run python tests in the root directory of the project:
```
nose2
```

To run website in development mode:
```sh
npm start
```

## Structure of scraped data
```
{
	'job_title': 'software developer',
	'date_posted': datetime.datetime(2022, 10, 5, 0, 0),
	'closing_date': datetime.datetime(2022, 10, 12, 0, 0),
	'url': 'something.com',
	'location': 'Moka',
	'employment_type': 'Permanent',
	'company': 'company',
	'salary': '10000-20000',
	'job_details': 'details',
	'timestamp': Sentinel: Value used to set a document field to the server timestamp.
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

# To-do 
- [ ] In `analyser` folder, make it easier to add/remove techs. Also make use of dictUtils.
- [ ] Automatically check for duplicates.
- [ ] update structure of scraped data in readme
- [ ] Add timeseries data viz
- [ ] add a workflow to backup database (and maybe release a public version)
- [ ] Fix : Riviere du Rempart district includes some nearby small islands.
- [ ] add statistics about job title. (for example : count most common jobs)