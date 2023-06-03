# Installation

Clone project:

```bash
git clone git@github.com:creme332/mauritius-tech-job-statistics.git
```

Install dependencies for frontend:

```bash
cd frontend
npm install
```

Install dependencies for backend:

```bash
cd backend
pip install -r requirements.txt
```

# Setup Firestore database 

[Create a Firestore database](https://firebase.google.com/docs/firestore/quickstart#create) and generate a service account key in JSON format.

Convert your service account key JSON to a base-64 encoded string by running the following command:

Generate a private key for your Firebase service account.

Create a Github Secret `SERVICE_ACCOUNT_KEY` with value given by `encoded_service_key` .

# Usage

## Run scraper

Run main program in terminal (or otherwise):

```sh
python src/main.py
```

> Scraping the website and analysing the data for the first time will take around 40 minutes. You can temporarily set `self.crawl_delay = 2` in `miner.py` to speed up the process.

## Run website

To run website in development mode:

```sh
cd frontend
npm start
```

# Testing

For backend:

```
cd backend
nose2
```
