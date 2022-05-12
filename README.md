# 🇲🇺 Job-Portal-Web-Scraper 2022
A web scraper for MyJobs.mu that checks the requirements of a particular job. For example, 
  - Look at all the ‘software developer’ jobs present in a job portal
  -  Analyze the job requirements 
  -  Plot a graph of frequency for each requirement using `graph` in python. 
  - Create a Top 10 skills in demand in Mauritius.
  - Create a pandas dataframe out of scraped data + maybe  use Jupyter Notebook

Inspired by the Stack Overflow Developer Survey, the goal of this Mauritian Developer Survey is to analyse the trends in technologies, in particular the technologies  in demand, in Mauritius.


Add table of contents
#  ⚒️ Methodology #

## 📝Data collection ##
In the span of x months, k unique IT job listings were scraped from [myjob.mu](https://www.myjob.mu/) using the BeautifulSoup library. These job listings were then saved in `data.csv` file.
![image](https://user-images.githubusercontent.com/65414576/167564657-213f37f0-bf25-4dbc-9ea0-21e39062e2bb.png)
> ⚠️URLS may no longer work as a job post is removed after a certain time. 

The URLS for each job are assumed to be unique but as a safety measure, following code is also used to prevent duplicates :
```python
DataFrame.drop_duplicates(subset=None, keep='first', inplace=False)
```

## 🔎 Data analysis ##
Data from the `data.csv` file was converted into a Panda dataframe. MatlPlotLib was then used for data visualisation.

# 📊 Results #
> ⚠️ **Interpret the following charts at your own discretion, keeping in mind the sample size and methodology used.**
> 
## Programming languages ## 
![image](https://user-images.githubusercontent.com/65414576/167571045-bccf3082-e958-4043-ac14-c3d4c5166c5f.png)

![image](https://user-images.githubusercontent.com/65414576/167336656-88849cb5-5529-494f-b495-a66a19e49bda.png)

![image](https://user-images.githubusercontent.com/65414576/167250513-31366d46-050b-40a8-ad3f-eadee5b45796.png)

## Web frameworks ##
![image](https://user-images.githubusercontent.com/65414576/167336522-59ef6c94-a46e-4dad-b8d9-e64e27f72d8c.png)

## Databases ##
![image](https://user-images.githubusercontent.com/65414576/167336593-e78bcf0d-8cb0-4745-8ca9-88069add29ba.png)

## Other libraries ##
![image](https://user-images.githubusercontent.com/65414576/167336578-879767b2-c77f-4df4-8589-db4cf9cafb96.png)

## Other tools ##
![image](https://user-images.githubusercontent.com/65414576/167336555-67b0ccff-e8e6-4e6c-af54-5f43b6916167.png)

## Salary vs Location ##
> ⚠️ **Only m% of job listings disclosed the salary**

![image](https://user-images.githubusercontent.com/65414576/168006545-46c48e67-9e05-4945-8299-bb6b8e2f1e59.png)
![image](https://user-images.githubusercontent.com/65414576/168006478-99248f68-6692-4533-8991-f8f6730899bc.png)


# 🎊 Conclusion #
Some technologies (SQL, Git, ...) are without any doubt highly in demand while other technologies (AWS, Clojure, Cloud technologies ...) are yet to take off in Mauritius. 
# 🌠Resouces used #
To create map of salary : https://towardsdatascience.com/a-complete-guide-to-an-interactive-geographical-map-using-python-f4c5197e23e0
To create lollipop chart :
# 🔮 Future work #
- Collect data from more job websites
- Create a folder to store all media files.
- Make images the same size on README
- Contrast the Stack Overflow Developer Survey with my survey
- Create a website to display data and add user interaction 
