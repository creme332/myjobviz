# Setup

## Prerequisites
- Node.js
- Python 3.1+
- Firebase account

## Installation

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

## Setup Firestore database 

1. [Create two Firestore databases](https://firebase.google.com/docs/firestore/quickstart#create) and generate a service account key in JSON format for each one.

2. Convert your service account key to a base-64 encoded string by using the `service_key_to_base64` function in `backend/src/utils/service_key.py` .

3. In `backend` folder, create a `.env` file with the following:
    ```
    SAK_MAIN_DB = YOUR_BASE64_KEY1
    SAK_STATS_DB = YOUR_BASE64_KEY2
    ```

> 🟡 **Note:** If you want to use Github Actions to run the project, you will have to create Github Secrets for the above keys.

## Usage

To run the project (without Github Actions), follow these instructions.

### Run scraper locally

To run the main program:

```sh
cd backend
python src/main.py
```

> Scraping the website and analysing the data for the first time will take around 40 minutes. You can temporarily set `self.load_duration = 3` in `miner.py` to speed up the process  but always keep this value above 2 seconds.

### Run website locally

To run website in development mode:

```sh
cd frontend
npm start
```

## Testing locally

To run backend tests:

```bash
cd backend
nose2
```
