# Mauritius Job Survey 📊 <a name="intro"></a> #
<img src="https://img.shields.io/badge/Python-3.9.7-orange">
<img src = "https://img.shields.io/badge/Panda-1.3.3-blue">
<img src = "https://img.shields.io/badge/BeautifulSoup-4.10.0-brightgreen">
<img src = "https://img.shields.io/badge/MatPlotLib-3.4.3-yellowgreen">
<img src = "https://img.shields.io/badge/Plotly-5.8.0-lightgrey">

Purpose : Analyse statistics of IT jobs in Mauritius.

#  Methodology #
In the span of $1$ months (1 May 2022 - 10 June 2022), $600$ unique **IT** job listings were scraped from [myjob.mu](https://www.myjob.mu/) using Python and BeautifulSoup library. The result was saved to a CSV file. Specific data (programming languages, databases, ...) from each job description were extracted. `MatlPlotLib` and `Plotly` were used to visualise the filtered data.


> ⚠️ **Interpret the following result at your own discretion, keeping in mind the sample size and methodology used.**

## Job count per district ##
![](Charts/choroplethmap.png)
*[View interactive map](https://creme332.github.io/InteractiveMap/)* 

## Technologies ##
![](Charts/LanguageChart.png)
![](Charts/WebChart.png)

![](Charts/DatabaseChart.png)
![](Charts/LibrariesChart.png)
![](Charts/ToolsChart.png)
![](Charts/WebLollipopChart.png)

![](Charts/OSChart.png)
![](Charts/CloudChart.png)
> ⚠️ **The percentage represents the percentage of jobs mentioning a particular criteria as opposed to the percentage of all jobs**


## Salary of IT jobs ##
![](Charts/SalaryChart.png)

> ⚠️ **Only around 100 job listings disclosed the salary**



# 🌠Resources used  <a name="resources"></a> #

[Tutorial on web scraping to CSV file](https://www.youtube.com/watch?v=RvCBzhhydNk&ab_channel=Pythonology)

[Interactive map](https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0) 

[Tutorial on how to create choropleth map](https://www.youtube.com/watch?v=aJmaw3QKMvk&ab_channel=IndianPythonista)

# 🔮 Future work <a name="future"></a> # 
- Collect data over a longer period
- Create a GitHub workflow to automate data collection process
- Collect data from more job websites
- Analyse how data varies with time
