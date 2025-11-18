# Setup Instructions

The following instructions assumes a Linux system but the steps for a Windows system are similar.

## Prerequisites

- Node.js
- Git
- Python 3.10+
- pip
- Firebase account

## Installation

```bash
# Clone repository
git clone git@github.com:creme332/myjobviz.git
cd myjobviz

# Install frontend dependencies
cd frontend
npm install --legacy-peer-deps

# Install backend dependencies
cd ../backend
pip install -r requirements.txt
```

**Note**:

- The `--legacy-peer-deps` flag is required because the project uses a version of `react-wordcloud` which is not compatible with React 18.
- It is recommended to create and activate a virtual environment before installing backend dependencies.

### Setup Firestore database 

1. [Create two Firestore databases](https://firebase.google.com/docs/firestore/quickstart#create) and generate a service account key in JSON format for each one.
2. Convert your service account key to a base-64 encoded string by using the `service_key_to_base64` function in `backend/src/utils/service_key.py` .
3. In `backend` folder, create a `.env` file with the following:
    ```
    SAK_MAIN_DB = YOUR_BASE64_KEY1
    SAK_STATS_DB = YOUR_BASE64_KEY2
    ```
4. If you're using your own Firebase project, update the Firebase configuration in `frontend/src/firebase-config.js` with your project's credentials:
    ```js
    const config = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
    appId: "YOUR_APP_ID",
    };
    ```
> [!NOTE]
> If you want to use Github Actions to run the project, you will have to create Github Secrets for the above keys.

## Usage

To run the project (without Github Actions), follow these instructions.

### Run scraper locally

To run the main program:

```sh
cd backend
python src/main.py
```

> Scraping the website and analyzing the data for the first time will take around 40 minutes. You can temporarily set `self.load_duration = 3` in `miner.py` to speed up the process but always keep this value above 2 seconds.

### Run website locally

To run website in development mode:

```sh
cd frontend
npm start
```

Visit `http://localhost:3000` to view the application.

### Testing

To run backend tests:

```bash
cd backend
nose2
```
