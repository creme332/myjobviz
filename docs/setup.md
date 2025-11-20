# Setup Instructions

The following instructions assumes a Linux system but the steps for a Windows system are similar.

## Prerequisites

- Node.js
- Git
- Python 3.10+
- pip
- Firebase account
- HuggingFace account (optional, for dataset backups)

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

### Setup HuggingFace Dataset Backups (Optional)

To enable automated monthly backups of your dataset to HuggingFace:

1. **Create a HuggingFace account** at [huggingface.co/join](https://huggingface.co/join)

2. **Generate an access token:**
   - Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Click "New token"
   - Give it a name (e.g., "myjobviz-backup")
   - Select "Write" permissions
   - Copy the token (starts with `hf_`)

3. **Configure the backup script:**
   - Open `backend/src/backup_to_huggingface.py`
   - Update these values:
     ```python
     USERNAME = "your-hf-username"  # Your HuggingFace username
     REPO_NAME = "mauritius-it-jobs"  # Your dataset repository name
     PRIVATE = False  # Set to True for private dataset
     ```

4. **For local backups:**
   - Add your token to the `.env` file:
     ```
     HF_TOKEN=hf_your_token_here
     ```
   - Run the backup script:
     ```bash
     cd backend
     python src/backup.py
     ```

5. **For automated GitHub Actions backups:**
   - Add GitHub Secrets to your repository:
     - Go to Settings → Secrets and variables → Actions
     - Add `HF_TOKEN` secret with your HuggingFace token
     - Add `FIREBASE_SERVICE_KEY` secret with your Firebase service account JSON
   
   - The workflow file at `.github/workflows/backup.yml` will automatically:
     - Run on the 1st of every month at 2 AM UTC
     - Can be triggered manually from the Actions tab
     - Backup both job data and statistics to HuggingFace

> [!TIP]
> You can manually trigger the backup workflow anytime from the GitHub Actions tab by clicking "Run workflow".

For detailed setup instructions and troubleshooting, see the [GitHub Actions Backup Guide](../backend/src/GITHUB_ACTIONS_SETUP.md).

## Usage

To run the project (without Github Actions), follow these instructions.

### Run scraper locally

To run the main program:

```sh
cd backend
python src/main.py
```

> Scraping the website and analyzing the data for the first time will take around 40 minutes. You can temporarily set `self.load_duration = 3` in `miner.py` to speed up the process but always keep this value above 2 seconds.

### Run backup locally

To backup your dataset to HuggingFace:

```sh
cd backend
python src/backup.py
```

The script will:
- Export all jobs from Firestore
- Create JSON and CSV files
- Generate metadata and statistics
- Upload everything to HuggingFace
- Create/update the dataset README

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
