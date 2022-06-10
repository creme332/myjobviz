# To-Do #
- [ ] - Make images the same size on README
- [ ] Idea : Manually merge several charts in 1 image. Keep pdf version in folder.
- [ ] For all barcharts, keep distance between bars constant
- [ ] Add pie chart for job types
- [ ] Add word cloud
- [ ] Publish results on GitHub pages
- [ ] Search each language/framework on site to see if spelling matches expected spelling


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

# 🇲🇺 Job Portal Web Scraper + Visualiser  <a name="intro"></a> #

Inspired by the Stack Overflow Developer Survey, the goal of this scraper is to analyse the trends in technologies in Mauritius.

#  ⚒️ Methodology  <a name="Methodology"></a> #

## 📝Data collection  <a name="collection"></a> ##
In the span of $2$ months (1 May 2022 - 1 July 2022), $600$ unique IT job listings were scraped from [myjob.mu](https://www.myjob.mu/) using the BeautifulSoup library. 
The result was saved to a CSV file.

More info here : 

## 🔎 Data analysis <a name="analysis"></a> ##
Specific data (programming languages, databases, ...) from each job description were extracted.

More info here : 


## 📈 Data visualisation ##
`MatlPlotLib` was used to visualise the filtered data.

`Plotly` was used to create the map.


# 📊 Results <a name="results"></a> #
> ⚠️ **Interpret the following charts at your own discretion, keeping in mind the sample size and methodology used.**
> 

## Programming languages <a name="prog"></a> ## 
<img src="https://user-images.githubusercontent.com/65414576/167571045-bccf3082-e958-4043-ac14-c3d4c5166c5f.png" width="600" height ="400">

## Web frameworks <a name="web"></a> ## 
![image](https://user-images.githubusercontent.com/65414576/167336522-59ef6c94-a46e-4dad-b8d9-e64e27f72d8c.png)

## Databases <a name="databases"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336593-e78bcf0d-8cb0-4745-8ca9-88069add29ba.png)

## Other libraries <a name="libraries"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336578-879767b2-c77f-4df4-8589-db4cf9cafb96.png)

## Other tools <a name="tools"></a> ##
![image](https://user-images.githubusercontent.com/65414576/167336555-67b0ccff-e8e6-4e6c-af54-5f43b6916167.png)

## Job count  ##

![image](https://user-images.githubusercontent.com/65414576/168541351-38da4b28-205c-4297-abab-eae8191e1513.png)

## Salary <a name="salary"></a> ##
> ⚠️ **Only m% of job listings disclosed the salary**

# 🎊 Conclusion <a name="conclusion"></a> # 
Some technologies (SQL, Git, ...) are without any doubt highly in demand while other technologies (AWS, Clojure, Cloud technologies ...) are yet to take off in Mauritius. 
# 🌠Resources used  <a name="resources"></a> #

Tutorial on web scraping to CSV file : https://www.youtube.com/watch?v=RvCBzhhydNk&ab_channel=Pythonology

map of salary : https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0

Tutorial on how to create chloropeth map : https://www.youtube.com/watch?v=aJmaw3QKMvk&ab_channel=IndianPythonista

# 🔮 Future work <a name="future"></a> # 
- Collect data from more job websites
- Analyse how data varies with time
