# Job-Portal-Web-Scraper 2022
A web scraper for MyJobs.mu that checks the requirements of a particular job. For example, 
  - Look at all the ‘software developer’ jobs present in a job portal
  -  Analyze the job requirements 
  -  Plot a graph of frequency for each requirement using `graph` in python. 
  - Create a Top 10 skills in demand in Mauritius.
  - Create a pandas dataframe out of scraped data + maybe  use Jupyter Notebook
  <img src="test.png" width="300">



Inspired by the Stack Overflow Developer Survey, the goal of this Mauritian Developer Survey is to analyse the trends in technologies, in particular the technologies  in demand, in Mauritius.

# 📝 Methodology #

## 👜Data collection ##
In the span of x months, k unique IT job listings were scraped from myjob.mu using BeautifulSoup library. These job listings were then saved in `data.csv` file.

## 🔎 Data analysis ##
Data from the `data.csv` file was converted into a Panda dataframe. MatlPlotLib was then used for data visualisation.

# 📊 Results #
## Programming languages ## 
![image](https://user-images.githubusercontent.com/65414576/167250513-31366d46-050b-40a8-ad3f-eadee5b45796.png)

## Web frameworks ##

## Databases ##

## Other libraries ##

## Other tools ##

# 🎊 Conclusion #
Some technologies (SQL, Git, ...) are without any doubt highly in demand while other technologies (AWS, Clojure, ...) are yet to take off in Mauritius. 
# 🔮 Future work #
- Collect data from more job websites
- Contrast the Stack Overflow Developer Survey with my survey
