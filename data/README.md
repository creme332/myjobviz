## Structure of scraped data ##
```
Columns = ['job_title', 'date_posted', 'closing date', 'URL', 'location', 'employment_type', 'company', 'salary', 'job_details']
```
![image](https://user-images.githubusercontent.com/65414576/172871961-5749afd3-bfa2-48bf-99ca-3519074bc59b.png)


#### Date format : `DD/MM/YY` ####
#### File format : `csv` ####
#### Encoding : `utf-8-sig` ####
#### Separator in csv file : `\t` ####

> ⚠️The URLs may not work as myjob.mu takes down a job post after a certain time. 

> ⚠️The job URL was used as a primary key during scraping to avoid duplicate entries.

> ⚠️ `job_title` and `job_details` can be in French or English. 

## Structure of GeoJson file ##
Sample :
```
{'id_0': 143, 'iso': 'MUS', 'name_0': 'Mauritius', 'id_1': 1, 'name_1': 'Agalega', 'hasc_1': 'MU.AG', 'ccn_1': 0, 'cca_1': None, 'type_1': 'Region', 'engtype_1': 'Region', 'nl_name_1': None, 'varname_1': None}
```

Source of geojson file for Mauritius districts : https://data.govmu.org/dkan/?q=dataset/mauritius-districts

The original geojson file contains some spelling mistakes (Rodrigues was mispelled for example) which were corrected in my version of the geojson file.
