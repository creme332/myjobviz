---
license: cc-by-4.0
task_categories:
- text-classification
- text-generation
language:
- en
tags:
- jobs
- mauritius
- IT
- career
pretty_name: Mauritius IT Jobs Dataset
size_categories:
- 1K<n<10K
---

# Mauritius IT Jobs Dataset

This dataset contains IT job listings scraped from [myjob.mu](http://myjob.mu), the primary job board in Mauritius.

This dataset is part of the [MyJobViz project](https://github.com/creme332/myjobviz), which provides visualization and analysis tools for the Mauritius IT job market.

## Dataset Description

- **Source:** myjob.mu
- **Geographic Focus:** Mauritius
- **Job Category:** Information Technology (IT) only
- **Collection Period:** 2022 - Present
- **Last Backup:** {timestamp}
- **Total Jobs:** {total_jobs}

## Dataset Structure

Each job listing contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `job_title` | string | Title of the job position |
| `company` | string | Name of the hiring company |
| `date_posted` | datetime | When the job was posted (Unix timestamp in ms) |
| `closing_date` | datetime | Application deadline (Unix timestamp in ms) |
| `location` | string | Job location within Mauritius |
| `employment_type` | string | Type of employment (e.g., Full-time, Trainee, Contract) |
| `salary` | string | Salary range or information |
| `job_details` | string | Full job description and requirements |
| `url` | string | Original job posting URL |
| `timestamp` | datetime | When the job was scraped (Unix timestamp in ms) |

### Example Entry

```json
{
    "job_title": "it helpdesk support - raw it services ltd",
    "company": "TAYLOR SMITH GROUP",
    "date_posted": 1676332800000,
    "closing_date": 1678924800000,
    "location": "Port Louis",
    "employment_type": "Trainee",
    "salary": "10,000 - 20,000",
    "job_details": "Your role will consist of providing support to the technical team...",
    "url": "http://myjob.mu/Jobs/IT-Helpdesk-Support-Raw-IT-141921.aspx",
    "timestamp": 1676427651200
}
```

## Files

- `jobs.json`: Complete job listings in JSON format
- `jobs.csv`: Complete job listings in CSV format (easier to preview)
- `metadata.json`: Backup metadata and statistics
{statistics_file_line}

## Usage

### Load with HuggingFace Datasets

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("{repo_id}")
print(dataset)
```

### Load with Pandas

```python
import pandas as pd

# From CSV
df = pd.read_csv("hf://datasets/{repo_id}/jobs.csv")

# From JSON
df = pd.read_json("hf://datasets/{repo_id}/jobs.json")

# Convert timestamps to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'], unit='ms')
df['closing_date'] = pd.to_datetime(df['closing_date'], unit='ms')
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
```

## Potential Use Cases

- **Job Market Analysis:** Analyze trends in Mauritius IT job market
- **Salary Research:** Study compensation patterns for IT roles
- **Skills Demand:** Identify most in-demand technologies and skills
- **Location Analysis:** Understand geographic distribution of IT jobs
- **Time Series Analysis:** Track job posting trends over time
- **NLP Tasks:** Job description classification, entity extraction, skill identification
- **Career Planning:** Research companies, job titles, and requirements in Mauritius IT sector

## Data Collection

Data is collected through automated web scraping of myjob.mu, focusing exclusively on IT-related job postings. The scraper runs periodically to capture new job listings.

**Scraping Code:** The code used to scrape and process this data is available at [github.com/creme332/myjobviz](https://github.com/creme332/myjobviz)

## Limitations

- Only includes IT jobs (other sectors not included)
- Geographic scope limited to Mauritius
- Dependent on data availability from source website
- Some fields may contain inconsistent formatting (e.g., whitespace in location field)
- Salary information may be missing or in various formats

## Statistics

The `statistics.json` file (if included) contains aggregated data on:
- Programming languages mentioned in job descriptions
- Technologies and frameworks (databases, cloud platforms, tools)
- Job title distributions
- Location distributions
- Salary ranges
- And more...

## Citation

If you use this dataset in your research or analysis, please cite:

```
Mauritius IT Jobs Dataset, scraped from myjob.mu
Part of the MyJobViz project: https://github.com/creme332/myjobviz
Available at: https://huggingface.co/datasets/{repo_id}
```

## License

This dataset is provided under CC-BY-4.0 license. The data is scraped from publicly available job listings.

## Backup History

This dataset is automatically updated with regular backups to preserve historical job market data.

**Last Updated:** {timestamp}