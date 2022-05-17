# -*- coding: utf-8 -*-
"""
Created on Wed May 11 10:05:03 2022
Python Version : 3.9.7
Panda version : 1.3.3
Summary : count word frequency from job details found in csv file
@author: user
"""
import pandas as pd
import numpy as np
import re
from csv import writer

data_source_filename = 'TESTING.csv'
jobs_df = pd.read_csv(data_source_filename)
jobs_df.drop_duplicates(
    subset=None, keep='first', inplace=False)  # drop duplicates

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)

# construct a separate csv file for word count


def AnalyseLanguages():
    # =============================================================================
    #     header = "C++,Java,Python,Javascript,\
    #     PHP,HTML,CSS,Node.js,Clojure,C#,Bash/Shell,\
    #     PowerShell,Kotlin,Rust,Typescript,SQL,Ruby,Dart"
    # =============================================================================

    language_count = {
        "C++": 0, "Java": 0, "Python": 0, "Javascript": 0, "PHP": 0,
        "HTML": 0, "CSS": 0, "Node.js": 0, "Clojure": 0,
        "C#": 0, "Bash/Shell": 0, "PowerShell": 0, "Kotlin": 0,
        "Rust": 0, "Typescript": 0, "SQL": 0, "Ruby": 0, "Dart": 0
    }

    # subtring testing : c++, c#, Node.js, bash/shell
    # languages that contain special characters.
    special_languages = ["C++", "Node.js", "C#", "Bash/Shell"]
    # These languages are never substrings of other another language.

    # token testing : java, python, javascript, php, html, ...
    standard_languages = ["Java", "Python", "Javascript",
                         "PHP", "HTML", "CSS", "Clojure",
                         "PowerShell", "Kotlin", "Rust", "Typescript",
                         "SQL", "Ruby", "Dart"]
    # Note Java is  a substring of Javascript
    # so substring method cannot be used here.
    # Ruby is a substring of "Ruby on Rails"


    # languages in language_count, special_languages, standard language must match exactly
    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"]

        # search languages using token method
        words = re.findall(r'\w+', jobs_details)  # uses any symbol as string
        # delimiters to create list of words from job_details
        for i in range (0,len(words)):
            for lang in standard_languages:
                if lang.lower() == words[i].lower():
                    if(lang=="Ruby"):
                        if(i<len(words)-2):
                            if(words[i+1].lower() != "on" and words[i+2].lower() != "rails"):
                                language_count[lang] += 1
                        else :
                            language_count[lang] += 1
                        
                    else :
                        language_count[lang] += 1

        # search special languages using substring
        for lang in special_languages:
            if lang.lower() in jobs_details.lower():
                language_count[lang] += 1

    # save language_count to a csv file
    lang_filename = "LanguageCountData.csv"
    tester = pd.DataFrame(language_count.items(), columns=['lang', 'freq'])
    tester.to_csv(lang_filename, sep='\t', encoding='utf-8-sig', index=False)

    # display(tester)


def AnalyseDatabases():
    databases_count = {
        "MySQL": 0, "PostgreSQL": 0, "SQLite": 0, "MongoDB": 0,
        "Microsoft SQL Server": 0, "Redis": 0, "MariaDB": 0, "Firebase": 0,
        "Elasticsearch": 0, "Oracle": 0, "DynamoDB": 0, "Cassandra": 0,
        "IBM DB2": 0, "Couchbase": 0
    }  # Will misflag Oracle Cloud as Oracle database

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"]

        for db in databases_count:
            if db.lower() in jobs_details.lower():
                databases_count[db] += 1

    # save databases_count to a csv file
    lang_filename = "DatabaseCountData.csv"
    tester = pd.DataFrame(databases_count.items(), columns=['lang', 'freq'])
    tester.to_csv(lang_filename, sep='\t', encoding='utf-8-sig', index=False)

    display(tester)


def AnalyseOtherTools():

    cloud_platforms = {"AWS": 0,
                       "Google Cloud Platform": 0,
                       "Microsoft Azure": 0,
                       "Heroku": 0,
                       "DigitalOcean": 0,
                       "Watson": 0,
                       "Oracle Cloud Infrastructure": 0
                       }

    web_frameworks = {"Svelte": 0,
                      "ASP.NET Core": 0,
                      "FastAPI": 0,
                      "React.js": 0,
                      "Vue.js": 0,
                      "Express": 0,
                      "Spring": 0,
                      "Ruby on Rails": 0,
                      "Angular": 0,
                      "Django": 0,
                      "Laravel": 0,
                      "Flask": 0,
                      "Gatsby": 0,
                      "Symfony": 0,
                      "ASP.NET": 0,
                      "jQuery": 0,
                      "Drupal": 0,
                      "Angular.js": 0
                      }

    libraries = {".NET Framework": 0,
                 "NumPy": 0,
                 ".NET Core": 0,
                 "Pandas": 0,
                 "TensorFlow": 0,
                 "React Native": 0,
                 "Flutter": 0,
                 "Keras": 0,
                 "PyTorch": 0,
                 "Cordova": 0,
                 "Apache Spark": 0,
                 "Hadoop": 0,
                 "Tableau": 0,
                 "Power BI": 0,
                 "Power Query": 0,
                 }

    other_tools = {
        "Git": 0,
        "Terraform": 0,
        "Kubernetes": 0,
        "Docker": 0,
        "Ansible": 0,
        "Yarn": 0,
        "Unreal Engine": 0,
        "Unity 3D": 0,
    }  # Git is a substring of GitHub

    # word frequency of Linux, GitHub

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"]
        words = re.findall(r'\w+', jobs_details)

        # search cloud platforms
        for cp in cloud_platforms:
            if cp.lower() in words.lower():
                cloud_platforms[cp] += 1

        # search web frameworkds
        for wb in web_frameworks:
            if wb.lower() in words.lower():
                web_frameworks[wb] += 1

        # search other
        for lb in libraries:
            if lb.lower() in words.lower():
                libraries[lb] += 1

        for tool in other_tools:
            if tool.lower() in words.lower():
                other_tools[tool] += 1


AnalyseDatabases()


# =============================================================================
# To-Do
# - Search each language/framework on site to see if spelling matches expected spelling
# - Create a separate file to store frequencies
# - Alternate spelling of React.js = ReactJS, React
# - Black background, change colors of bars
# - add xlabel, ylabel to parameters
#    https://towardsdatascience.com/donut-plot-with-matplotlib-python-be3451f22704
#   create donut plot with percentage
# =============================================================================
#
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
#
# =============================================================================
# =============================================================================
# =============================================================================
