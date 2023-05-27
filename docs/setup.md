# Setup Firestore database 
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

## Run scraper
Run main program in terminal (or otherwise):
```sh
python src/main.py
```
> Scraping the website and analysing the data for the first time will take around 40 minutes. You can temporarily set  `self.crawl_delay = 2` in `miner.py` to speed up the process.

Run python tests in the root directory of the project:
```
nose2
```
## Run website
To run website in development mode:
```sh
npm start
```

## Structure of scraped data
```python
{
	'job_title':  string,
	'date_posted': datetime,
	'closing_date': datetime,
	'url': string,
	'location': string,
	'employment_type': string,
	'company': string,
	'salary': string,
	'job_details': string,
	'timestamp': Sentinel: Value used to set a document field to the server timestamp.
}
```

### Notes
- The URLs scraped may not work as myjob.mu takes down a job post after a certain time. 
- The job URL was used as a primary key during scraping to avoid duplicate entries.
- `job_title` and `job_details` can be in French or English. 
- `date_posted` and `closing_date` are strings which follow `DD/MM/YYYY` format.





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