# myjobviz setup

The following instructions assumes a Linux system but the steps for a Windows system are similar.

## Installation

### Prerequisites
- Node.js
- Git
- Python 3.1+
- Firebase account

Clone project:

```bash
git clone git@github.com:creme332/myjobviz.git
```
Navigate to project:
```
cd myjobviz
```
Navigate to `myjobviz/frontend` and install dependencies for frontend:

```bash
npm install --legacy-peer-deps
```
> 🟠 **Note**: The `--legacy-peer-deps` flag is required because the project uses a version of `react-wordcloud` which is not compatible with React 18.

Navigate to `myjobviz/backend` and install dependencies for backend:

```bash
pip install -r requirements.txt
```
> 🟠 **Note**: It is recommended to create and activate a virtual environment before installing backend dependencies.

### Setup Firestore database 

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

### Testing

To run backend tests:

```bash
cd backend
nose2
```
