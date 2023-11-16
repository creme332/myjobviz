# Structure of scraped data

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

Example of scraped data in JSON:

```js
  {
      "timestamp": 1676427651200,
      "company": "TAYLOR SMITH GROUP",
      "date_posted": 1676332800000,
      "closing_date": 1678924800000,
      "salary": "10,000 - 20,000",
      "url": "http://myjob.mu/Jobs/IT-Helpdesk-Support-Raw-IT-141921.aspx",
      "job_details": "\nYour role will consist of providing support to the technical team by participating...",
      "employment_type": "Trainee",
      "location": "\nPort Louis ",
      "job_title": "it helpdesk support - raw it services ltd"
  },
```

More examples of scraped data can be found in `backend/tests/data/sample_jobs.json`

## Notes
* The URLs scraped may not work as `myjob.mu` takes down a job post after a certain time. 
* The job URL was assumed to be a "primary key" during scraping to avoid duplicate entries.
* `job_title` and `job_details` can be in French or English. 
* `date_posted` and `closing_date` are timestamps which follow `DD/MM/YYYY` format.
* Use https://vector.rocks/ to edit geojson for choropleth map.
