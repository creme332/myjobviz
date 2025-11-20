from classes.database import Database
from utils.service_key import get_service_account_key
from huggingface_hub import HfApi, create_repo, login
from datetime import datetime
import os
import json
from dotenv import load_dotenv, find_dotenv


def backup_to_huggingface(
    hf_token: str,
    repo_name: str,
    username: str,
    private: bool = False,
    include_statistics: bool = True
):
    """
    Backs up Firebase database to HuggingFace datasets.

    Args:
        hf_token (str): HuggingFace API token (get from https://huggingface.co/settings/tokens)
        repo_name (str): Name of the dataset repository (e.g., "job-board-backup")
        username (str): Your HuggingFace username
        private (bool): Whether to make the dataset private. Defaults to False.
        include_statistics (bool): Whether to backup statistics collection. Defaults to True.
    """

    print("Connecting to Firebase...")
    main_db = Database(get_service_account_key(True))

    # Create backup directory
    backup_dir = "backup_temp"
    os.makedirs(backup_dir, exist_ok=True)

    # Get current timestamp for versioning
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    print("Exporting jobs collection...")
    df = main_db.get_dataframe()

    # Save jobs as JSON
    jobs_file = os.path.join(backup_dir, "jobs.json")
    df.to_json(jobs_file, orient='records', indent=2, date_format='iso')
    print(f"Exported {len(df)} jobs")

    # Save jobs as CSV (easier to preview on HuggingFace)
    csv_file = os.path.join(backup_dir, "jobs.csv")
    df.to_csv(csv_file, index=False)

    # Create metadata file
    metadata = {
        "backup_timestamp": timestamp,
        "dataset_info": {
            "name": "Mauritius IT Jobs Dataset",
            "source": "myjob.mu",
            "geographic_scope": "Mauritius",
            "job_category": "Information Technology (IT)",
            "collection_period_start": "2022",
            "collection_period_end": timestamp.split("_")[0]
        },
        "statistics": {
            "total_jobs": len(df),
            "database_size": main_db.get_size(),
            "last_job_update": str(main_db.get_last_update_date())
        },
        "data_schema": {
            "job_title": "string - Title of the job position",
            "company": "string - Name of the hiring company",
            "date_posted": "datetime - When job was posted (Unix timestamp ms)",
            "closing_date": "datetime - Application deadline (Unix timestamp ms)",
            "location": "string - Job location within Mauritius",
            "employment_type": "string - Type of employment (Full-time, Trainee, etc.)",
            "salary": "string - Salary range or information",
            "job_details": "string - Full job description and requirements",
            "url": "string - Original job posting URL",
            "timestamp": "datetime - When job was scraped (Unix timestamp ms)"
        },
        "description": "IT job listings scraped from myjob.mu, the primary job board in Mauritius"
    }

    metadata_file = os.path.join(backup_dir, "metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)

    # Optionally backup statistics
    if include_statistics:
        print("Exporting statistics...")
        stats = {
            "metadata": main_db.get_doc(main_db.metadata_ref),
            "cloud_data": main_db.get_doc(main_db.cloud_data_ref),
            "db_data": main_db.get_doc(main_db.db_data_ref),
            "lang_data": main_db.get_doc(main_db.lang_data_ref),
            "lib_data": main_db.get_doc(main_db.lib_data_ref),
            "loc_data": main_db.get_doc(main_db.loc_data_ref),
            "os_data": main_db.get_doc(main_db.os_data_ref),
            "salary_data": main_db.get_doc(main_db.salary_data_ref),
            "tools_data": main_db.get_doc(main_db.tools_data_ref),
            "web_data": main_db.get_doc(main_db.web_data_ref),
            "job_title_data": main_db.get_doc(main_db.job_title_data_ref)
        }

        stats_file = os.path.join(backup_dir, "statistics.json")
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

    # Upload to HuggingFace
    print("\nConnecting to HuggingFace...")
    login(token=hf_token)
    api = HfApi()

    repo_id = f"{username}/{repo_name}"

    # Create repository if it doesn't exist
    try:
        print(f"Creating/accessing repository: {repo_id}")
        create_repo(
            repo_id=repo_id,
            repo_type="dataset",
            private=private,
            exist_ok=True
        )
    except Exception as e:
        print(f"Repository might already exist: {e}")

    # Upload files
    print("\nUploading files to HuggingFace...")

    files_to_upload = [
        ("jobs.json", "Primary jobs data in JSON format"),
        ("jobs.csv", "Primary jobs data in CSV format"),
        ("metadata.json", "Backup metadata")
    ]

    if include_statistics:
        files_to_upload.append(("statistics.json", "Database statistics"))

    for filename, description in files_to_upload:
        file_path = os.path.join(backup_dir, filename)
        print(f"  Uploading {filename}...")
        api.upload_file(
            path_or_fileobj=file_path,
            path_in_repo=filename,
            repo_id=repo_id,
            repo_type="dataset",
            commit_message=f"Backup: {timestamp} - {description}"
        )

    # Read and populate README template
    readme_template_path = "README_TEMPLATE.md"

    if not os.path.exists(readme_template_path):
        raise FileNotFoundError(
            f"README template not found at {readme_template_path}. "
            "Please ensure README_TEMPLATE.md exists in the same directory."
        )

    with open(readme_template_path, 'r') as f:
        readme_content = f.read()

    # Replace template variables
    readme_content = readme_content.replace("{timestamp}", timestamp)
    readme_content = readme_content.replace("{total_jobs}", f"{len(df):,}")
    readme_content = readme_content.replace("{repo_id}", repo_id)
    stats_line = "- `statistics.json`: Database statistics and aggregations (skills, technologies, locations, etc.)" if include_statistics else ""
    readme_content = readme_content.replace(
        "{statistics_file_line}", stats_line)

    readme_file = os.path.join(backup_dir, "README.md")
    with open(readme_file, 'w') as f:
        f.write(readme_content)

    print("  Uploading README.md...")
    api.upload_file(
        path_or_fileobj=readme_file,
        path_in_repo="README.md",
        repo_id=repo_id,
        repo_type="dataset",
        commit_message=f"Update README: {timestamp}"
    )

    print(f"\n✓ Backup complete!")
    print(f"✓ Dataset URL: https://huggingface.co/datasets/{repo_id}")
    print(f"✓ Total files uploaded: {len(files_to_upload) + 1}")

    # Cleanup
    print("\nCleaning up temporary files...")
    for filename, _ in files_to_upload:
        os.remove(os.path.join(backup_dir, filename))
    os.remove(readme_file)
    os.rmdir(backup_dir)


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    # Configuration
    HF_TOKEN = os.getenv('HF_TOKEN')
    USERNAME = "goated69"
    REPO_NAME = "mauritius-it-jobs"
    PRIVATE = False  # Set to True if you want a private dataset

    if not HF_TOKEN:
        print("Error: Please set HF_TOKEN environment variable")
        print("Get your token from: https://huggingface.co/settings/tokens")
        exit(1)

    backup_to_huggingface(
        hf_token=HF_TOKEN,
        repo_name=REPO_NAME,
        username=USERNAME,
        private=PRIVATE,
        include_statistics=False
    )
