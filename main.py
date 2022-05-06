# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
from math import log10
from matplotlib import cm


    
def CircularBarChart(dictionary, filename):
    #filter out data which have a count of 0 
    for key in list(dictionary):
        if dictionary[key] == 0:
            dictionary.pop(key, None)
            
    labels = list(dictionary.keys())
    data = list(dictionary.values())
    
    #number of data points
    n = len(data)
    #find max value for full ring
    k = 10 ** int(log10(max(data)))
    m = k * (1 + max(data) // k)
    
    #radius of donut chart
    r = 1.5
    #calculate width of each ring
    w = r / n 
    
    #create colors along a chosen colormap
    colors = [cm.terrain(i / n) for i in range(n)]
    
    #create figure, axis
    fig, ax = plt.subplots()
    ax.axis("equal")
    
    #create rings of donut chart
    for i in range(n):
        #hide labels in segments with textprops: alpha = 0 - transparent, alpha = 1 - visible
        innerring, _ = ax.pie([m - data[i], data[i]], radius = r - i * w, startangle = 90, labels = ["", labels[i]], labeldistance = 1 - 1 / (1.5 * (n - i)), textprops = {"alpha": 0}, colors = ["white", colors[i]])
        plt.setp(innerring, width = w, edgecolor = "white")
    
    plt.legend()
    plt.savefig(filename)
    
def BarChart(dictionary, filename):
    #filter out data which have a count of 0 
    for lang in list(dictionary):
        if dictionary[lang] == 0:
            dictionary.pop(lang, None)

    plt.figure(figsize=(10, 3))  # width:20, height:3
    plt.bar(range(len(dictionary)), dictionary.values(), align='center', width=0.3)
    plt.xticks(range(len(dictionary)), dictionary.keys())
    
    # Show graph
    plt.savefig(filename)
    
#  try venn diagram : HTML, CSS, Javascript
def plotLanguages(languages): # pie chart not approprite here becasuse sum != job count. use histogram
    #filter out languages which have not been used at all
    for lang in list(languages):
        if languages[lang] == 0:
            languages.pop(lang, None)

    languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    x, y = zip(*languages) # unpack a list of pairs into two tuples
    for i in languages:
        print(i[0], i[1])
    # create a figure and set different background
    fig = plt.figure()
    fig.patch.set_facecolor('black')
     
    # Change color of text
    plt.rcParams['text.color'] = 'white'
     
    # Create a circle at the center of the plot
    my_circle=plt.Circle( (0,0), 0.7, color='black')
     
    # Pieplot + circle on it
    plt.pie(y, labels=x, shadow = True, autopct='%1.1f%%')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.savefig('filename.pdf')
    #plt.show()

    
def main():
    default_page_url = 'https://www.myjob.mu/ShowResults.aspx?Keywords=&Location=&Category=39&Recruiter=Company&Page=' 
    developer_jobs_count = 0

    languages = {
            "C++":0, "Java":0, "Python":0, "Javascript":0, "PHP":0, "HTML":0, "CSS":0, "Node.js":0, "Clojure":0,
            "C#" :0, "Bash/Shell":0, "PowerShell":0, "Kotlin":0,
            "Rust":0, "Typescript":0, "SQL":0, "Ruby":0, "Dart":0
            }

    databases = {
        "MySQL" : 0, "PostgreSQL" : 0, "SQLite" : 0, "MongoDB" : 0,
        "Microsoft SQL Server" : 0, "Redis" : 0, "MariaDB" : 0, "Firebase" : 0,
        "Elasticsearch" : 0, "Oracle" : 0, "DynamoDB" : 0, "Cassandra" : 0,
        "IBM DB2" : 0, "Couchbase" : 0
        }

    cloud_platforms = {}

    web_frameworks  = {}

    tools = {}
                #if(job_module.find('a',itemprop='hiringOrganization') != None):
                    #company_name = job_module.find('a',itemprop='hiringOrganization').text
                #date_posted = job_module.find('li',itemprop='datePosted').text.replace('Added ','')
    for page_number in range(1,2):
        
        html_text = requests.get(default_page_url + str(page_number)).text
        soup =  BeautifulSoup(html_text,'lxml')
        job_modules = soup.find_all('div',class_='module job-result') # find all job modules on current page
        
        for job_module in job_modules :
            
            job_title = job_module.find('h2',itemprop='title').text.lower()
            keywords = ["developer", "développeur", "engineer", "ingénieur"]
            
            if(any(substring in job_title for substring in keywords)): #if title contains keywords
                developer_jobs_count+=1
                
                # Extracting job details from Show More 
                show_more_url = "http://myjob.mu" + job_module.find('a', href = True, class_='show-more')['href']
                show_more_page_text = requests.get(show_more_url).text
                soup1 =  BeautifulSoup(show_more_page_text,'lxml')
                jobs_details = soup1.find('div', class_='job-details').text

                #search languages
                for lang in languages:
                    if lang.lower() in jobs_details.lower():
                        languages[lang]+=1
                        
                #search databases
                for db in databases:
                    if db.lower() in jobs_details.lower():
                        databases[db]+=1
                        
                #search cloud platforms
# =============================================================================
#                 for cp in cloud_platforms:
#                     if cp.lower() in jobs_details.lower():
#                         cloud_platforms[lang]+=1
#                         
#                 #search web frameworkds
#                 for wb in web_frameworks:
#                     if wb.lower() in jobs_details.lower():
#                         web_frameworks[wb]+=1
#                         
#                 #search other tools
#                 for tool in tools:
#                     if tool.lower() in jobs_details.lower():
#                         tools[tool]+=1
# =============================================================================

    #HorizontalBarChart(languages, "chart1.pdf")
    #BarChart(languages,"barchartlanguages.pdf")
    #CircularBarChart(databases,"barchartdatabases.pdf")

    print(developer_jobs_count)

main()
