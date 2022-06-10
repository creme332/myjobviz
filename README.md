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
6. [Future work](#future) 

# 🇲🇺 Job Portal Web Scraper + Visualiser  <a name="intro"></a> #

Inspired by the Stack Overflow Developer Survey, the goal of this scraper is to analyse the trends in technologies in Mauritius.

#  ⚒️ Methodology  <a name="Methodology"></a> #

## 📝Data collection  <a name="collection"></a> ##
In the span of $2$ months (1 May 2022 - 1 July 2022), $600$ unique IT job listings were scraped from [myjob.mu](https://www.myjob.mu/) using Python and BeautifulSoup library. 
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
![](Charts/LanguageChart.png)

## Web frameworks <a name="web"></a> ## 
![](Charts/WebChart.png)

## Databases <a name="databases"></a> ##
![](Charts/DatabaseChart.png)

## Other libraries <a name="libraries"></a> ##
![](Charts/LibrariesChart.png)
## Other tools <a name="tools"></a> ##
![](Charts/ToolsChart.png)
## Job count  ##
![]()
## Operating systems <a name=""></a> ##
![](Charts/OSChart.png)
> ⚠️ **The percentage represents the percentage of jobs mentioning any operating system $\ne$ percentage of all jobs**

## Cloud platforms <a name=""></a> ##
![](Charts/CloudChart.png)
> ⚠️ **The percentage represents the percentage of jobs mentioning any cloud platform $\ne$ percentage of all jobs**

## Salary <a name="salary"></a> ##
![](Charts/SalaryChart.png)
> ⚠️ **Only around 100 job listings disclosed the salary**

# 🌠Resources used  <a name="resources"></a> #

[Tutorial on web scraping to CSV file](https://www.youtube.com/watch?v=RvCBzhhydNk&ab_channel=Pythonology)

[Interactive map](https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0) 

[Tutorial on how to create chloropeth map](https://www.youtube.com/watch?v=aJmaw3QKMvk&ab_channel=IndianPythonista)

# 🔮 Future work <a name="future"></a> # 
- Collect data from more job websites
- Analyse how data varies with time
- Deploy interactive map on GitHub Pages
- 
