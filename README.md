# To-Do #
- [ ] https://towardsdatascience.com/donut-plot-with-matplotlib-python-be3451f22704 create donut plot with percentage
- [ ] Use percentages instead of frequency in barcharts
- [ ] Barchart for each category is a unique colour. (orange for programming lang, blue for database,...)
- [ ] Add pie chart for job types
- [ ] Add word cloud
- [ ] Publish results on GitHub pages
- [ ] Search each language/framework on site to see if spelling matches expected spelling
- [ ] Data analysis : Is degree required ?
- [ ] Convert opening and closing date in csv file to US date format then sort.

# Table of contents #
1. [Introduction](#intro)
2. [Methodology](#Methodology)
   1. [Data collection](#collection)
   2. [Data analysis](#analysis)
3. [Results](#results)
   1. [Programming languages](#prog)
   2. [Web frameworks](#web)
   3. [Databases](#databases)
   4. [Other libraries](#libraries)
   5. [Other tools](#tools)
   6. [Salary](#salary)
5. [Resources used](#resources)
6. [Conclusion](#conclusion)
7. [Future work](#future) 

# 🇲🇺 Job-Portal-Web-Scraper 2022  <a name="intro"></a> #

Inspired by the Stack Overflow Developer Survey, the goal of this survey is to analyse the trends in technologies in Mauritius.

#  ⚒️ Methodology  <a name="Methodology"></a> #

## 📝Data collection  <a name="collection"></a> ##
In the span of $x$ months (1 May 2022 - 1 July 2022), $k$ unique IT job listings were scraped from [myjob.mu](https://www.myjob.mu/) using the BeautifulSoup library. These job listings were then saved in `data.csv` file. 
![image](https://user-images.githubusercontent.com/65414576/167564657-213f37f0-bf25-4dbc-9ea0-21e39062e2bb.png)
> ⚠️The URLs in the csv file may no longer work as myjob.mu takes down a job post after a certain time. 

> ⚠️The job URL was used as a primary key.

### Dependencies ###
```
Python : 3.9.7
Panda : 1.3.3
BeautifulSoup : 4.10.0
MatPlotLib : 3.4.3
Plotly : 5.8.0
```
### Format used for data storage ###
To save :
```python
df.to_csv("file.csv", sep = '\t', encoding = 'utf-8-sig', index = False)
```

To read :
```python
df = pd.read_csv("file.csv", sep = '\t')
```

## 🔎 Data analysis <a name="analysis"></a> ##
Relevant data (salary, languages, databases, ...) from each job description was extracted and saved to new files.
`MatlPlotLib` and `Plotly` were then used to visualise the filtered data.

# 📊 Results <a name="results"></a> #
> ⚠️ **Interpret the following charts at your own discretion, keeping in mind the sample size and methodology used.**
> 

## Programming languages <a name="prog"></a> ## 
![image](https://user-images.githubusercontent.com/65414576/167571045-bccf3082-e958-4043-ac14-c3d4c5166c5f.png)

![image](https://user-images.githubusercontent.com/65414576/167336656-88849cb5-5529-494f-b495-a66a19e49bda.png)

![image](https://user-images.githubusercontent.com/65414576/167250513-31366d46-050b-40a8-ad3f-eadee5b45796.png)

## Web frameworks <a name="web"></a> ## 
![image](https://user-images.githubusercontent.com/65414576/167336522-59ef6c94-a46e-4dad-b8d9-e64e27f72d8c.png)

## Databases <a name="databases"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336593-e78bcf0d-8cb0-4745-8ca9-88069add29ba.png)

## Other libraries <a name="libraries"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336578-879767b2-c77f-4df4-8589-db4cf9cafb96.png)

## Other tools <a name="tools"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336555-67b0ccff-e8e6-4e6c-af54-5f43b6916167.png)

## Salary vs Location <a name="salary"></a> ##
> ⚠️ **Only m% of job listings disclosed the salary**

![image](https://user-images.githubusercontent.com/65414576/168541351-38da4b28-205c-4297-abab-eae8191e1513.png)


![image](https://user-images.githubusercontent.com/65414576/168006545-46c48e67-9e05-4945-8299-bb6b8e2f1e59.png)
![image](https://user-images.githubusercontent.com/65414576/168006478-99248f68-6692-4533-8991-f8f6730899bc.png)


# 🎊 Conclusion <a name="conclusion"></a> # 
Some technologies (SQL, Git, ...) are without any doubt highly in demand while other technologies (AWS, Clojure, Cloud technologies ...) are yet to take off in Mauritius. 
# 🌠Resources used  <a name="resources"></a> #

Tutorial on web scraping to CSV file : https://www.youtube.com/watch?v=RvCBzhhydNk&ab_channel=Pythonology

map of salary : https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0

lollipop chart :

Source of geojson file for Mauritius districts : https://data.govmu.org/dkan/?q=dataset/mauritius-districts

Tutorial on how to create chloropeth map : https://www.youtube.com/watch?v=aJmaw3QKMvk&ab_channel=IndianPythonista

# 🔮 Future work <a name="future"></a> # 
- Collect data from more job websites
- Create a folder to store all media files.
- Make images the same size on README
- Contrast the Stack Overflow Developer Survey with my survey
- Create a website to display data and add user interaction 
