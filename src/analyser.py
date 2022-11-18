#!venv/bin/python3
"""
This module extracts useful statistics from the database which
will be used later by `visualiser.py`
"""
import pandas as pd
import re
from classes.database import Database

jobs_df = Database().get_dataframe()


def AnalyseLanguages(destination_filename):
    """Analyses popularity of programming langugages from job descriptions.
    This is done by creating a table of language vs frequency.

    Args:
        destination_filename (str): path where statistics will be saved
    """
    language_count = {
        "C++": 0, "Java": 0, "Python": 0, "Javascript": 0, "PHP": 0,
        "HTML": 0, "CSS": 0, "Clojure": 0,
        "C#": 0, "Bash": 0, "Shell": 0, "PowerShell": 0, "Kotlin": 0,
        "Rust": 0, "Typescript": 0, "SQL": 0, "Ruby": 0, "Dart": 0
    }

    # languages that contain special characters.
    special_languages = ["C++", "C#"]
    # These languages are never substrings of other another language.

    # token testing : java, python, javascript, php, html, ...
    standard_languages = ["Java", "Python", "Javascript",
                          "PHP", "HTML", "CSS", "Clojure",
                          "PowerShell", "Kotlin", "Rust", "Typescript",
                          "SQL", "Ruby", "Dart", "Bash", "Shell"]
    # Java is  a substring of Javascript
    # SQL is a subtstring of mySQL, NoSQL
    # Ruby is a substring of "Ruby on Rails"
    # so substring method cannot be used here.

    # languages in language_count, special_languages,
    # standard language must match exactly

    for row in range(len(jobs_df)):  # for each collected job details
        jobs_details = jobs_df.loc[row, "job_details"].lower()

        # 1st search : search for languages using token method
        # any symbol is used as string delimiter

        # list of words in job details
        words = re.findall(r'\w+', jobs_details)

        for i in range(0, len(words)):  # for each word in job details
            for lang in standard_languages:  # search for standard languages

                if lang.lower() == words[i]:
                    # distinguish between ruby and ruby on rails
                    if (lang.lower() == "ruby"):
                        if (i > len(words)-3):
                            # language is definitely ruby
                            language_count[lang] += 1
                        else:
                            if (words[i+1].lower() != "on" and
                               words[i+2].lower() != "rails"):
                                # current word is not part of ruby on rails
                                language_count[lang] += 1
                    else:
                        language_count[lang] += 1  # other standard language

        # search special languages using substring
        for lang in special_languages:
            if lang.lower() in jobs_details:
                language_count[lang] += 1

    # save language_count to a csv file
    tester = pd.DataFrame(language_count.items(), columns=[
                          'Language', 'Frequency'])
    tester.to_csv(destination_filename, sep='\t',
                  encoding='utf-8-sig', index=False)


def AnalyseDatabases(destination_filename):
    """Analyses popularity of databases from job descriptions. This is done
    by creating a table of database vs frequency.

    Args:
        destination_filename (str): path where statistics will be saved
    """
    databases_count = {
        "MySQL": 0, "PostgreSQL": 0, "SQLite": 0, "MongoDB": 0,
        "Microsoft SQL Server": 0, "Redis": 0, "MariaDB": 0, "Firebase": 0,
        "Elasticsearch": 0, "Oracle": 0, "DynamoDB": 0, "Cassandra": 0,
        "IBM DB2": 0, "Couchbase": 0, "NoSQL": 0
    }  # Will misflag Oracle Cloud as Oracle database

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"].lower()  # lower case

        # use substring method for database names with more than 1 word
        if ("microsoft sql server" in jobs_details):
            databases_count["Microsoft SQL Server"] += 1

        if ("ibm db2" in jobs_details):
            databases_count["IBM DB2"] += 1

        # use token method for single-word databases
        words = re.findall(r'\w+', jobs_details)

        for db in databases_count:
            if db.lower() in words:
                databases_count[db] += 1

    # save databases_count to a csv file
    lang_filename = destination_filename
    tester = pd.DataFrame(databases_count.items(), columns=[
                          'Database', 'Frequency'])
    tester.to_csv(lang_filename, sep='\t', encoding='utf-8-sig', index=False)


def AnalyseWebFrameworks(destination_filename):
    """Analyses popularity of web frameworks from job descriptions.
    This is done by creating a table of web frameworks vs frequency.

    Args:
        destination_filename (str): path where statistics will be saved
    """
    web_frameworks_count = {"Svelte": 0,
                            "ASP.NET": 0,
                            "FastAPI": 0,
                            "React": 0,
                            "Vue.js": 0,  # or Vue if  english job description
                            "Express": 0,
                            "Spring": 0,
                            "Ruby on Rails": 0,
                            "Django": 0,
                            "Laravel": 0,
                            "Flask": 0,
                            "Gatsby": 0,
                            "Symfony": 0,
                            "jQuery": 0,
                            "Drupal": 0,
                            "Angular.js": 0,
                            "Angular": 0
                            }
    special_web_frameworks = ["Ruby on Rails", "ASP.NET"]

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"]

        if "Vue" in jobs_details:
            web_frameworks_count["Vue.js"] += 1

        jobs_details = jobs_details.lower()

        for wb in special_web_frameworks:  # substring method
            if wb.lower() in jobs_details:
                web_frameworks_count[wb] += 1

        # use token method for single-word databases
        words = re.findall(r'\w+', jobs_details)  # words are lower case

        for i in range(0, len(words)):  # for each word in job details
            for lang in web_frameworks_count:  # search for standard languages

                if lang.lower() == words[i]:

                    if (words[i] == "angularjs"):  # AngularJS spelling
                        web_frameworks_count["Angular.js"] += 1
                    # distinguish between angular and angular js
                    if (words[i] == "angular"):
                        if (i < len(words)-1):
                            if (words[i+1] == "js"):
                                web_frameworks_count["Angular.js"] += 1
                            else:
                                web_frameworks_count["Angular"] += 1
                        else:
                            web_frameworks_count["Angular"] += 1

                    else:
                        web_frameworks_count[lang] += 1

    tester = pd.DataFrame(web_frameworks_count.items(), columns=[
                          'WebFrameworks', 'Frequency'])
    tester.to_csv(destination_filename, sep='\t',
                  encoding='utf-8-sig', index=False)


def AnalyseOtherTools(file_path):
    """Analyses popularity of tools from job descriptions.

    Args:
        destination_filename (str): path where statistics will be saved
    """
    cloud_platforms = {"AWS": 0,
                       "Google Cloud": 0,
                       "Azure": 0,
                       "Heroku": 0,
                       "DigitalOcean": 0,
                       "Watson": 0,
                       "Oracle Cloud Infrastructure": 0
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
        "Node.js": 0,
        "Docker": 0,
        "Ansible": 0,
        "Yarn": 0,
        "Unreal Engine": 0,
        "Unity 3D": 0,
        "GitHub": 0,
    }  # Git is a substring of GitHub

    operating_system_count = {
        "Windows": 0,
        "Mac": 0,
        "Linux": 0,
    }

    for row in range(len(jobs_df)):
        jobs_details = jobs_df.loc[row, "job_details"].lower()

        # search cloud platforms
        for cp in cloud_platforms:
            if cp.lower() in jobs_details:
                cloud_platforms[cp] += 1

        # search libraries
        for lb in libraries:
            if lb.lower() in jobs_details:
                libraries[lb] += 1

        for tool in other_tools:
            if tool != "Node.js":
                # must distinguish between git and github
                if tool.lower() in jobs_details and tool != "Git":
                    other_tools[tool] += 1
        if "nodejs" in jobs_details or "node.js" in jobs_details:
            other_tools["Node.js"] += 1
        words = re.findall(r'\w+', jobs_details)
        if "git" in words:
            other_tools["Git"] += 1

        for os in operating_system_count:
            if os.lower() in jobs_details:
                operating_system_count[os] += 1

    # save cloud platforms
    cloud_df = pd.DataFrame(cloud_platforms.items(), columns=[
        'CloudPlatforms', 'Frequency'])
    cloud_df.to_csv(file_path + "CloudData.csv", sep='\t',
                    encoding='utf-8-sig', index=False)

    # save libraries
    libraries_df = pd.DataFrame(libraries.items(), columns=[
        'Libraries', 'Frequency'])
    libraries_df.to_csv(file_path + "LibrariesData.csv", sep='\t',
                        encoding='utf-8-sig', index=False)

    # save tools
    tools_df = pd.DataFrame(other_tools.items(), columns=[
        'Tools', 'Frequency'])
    tools_df.to_csv(file_path + "ToolsData.csv", sep='\t',
                    encoding='utf-8-sig', index=False)

    # save OS
    os_df = pd.DataFrame(operating_system_count.items(), columns=[
        'OS', 'Frequency'])
    os_df.to_csv(file_path + "OSData.csv", sep='\t',
                 encoding='utf-8-sig', index=False)


def AnalyseSalary(destination_filename):
    """Identifies the most common salary ranges.

    Args:
        destination_filename (str): path where statistics will be saved.
    """
    df = jobs_df.groupby(["salary"], as_index=False).size()

    df = df[df['salary'] != 'Not disclosed']
    df = df[df['salary'] != 'Negotiable']
    df = df[df['salary'] != 'See description']

    df.to_csv(destination_filename, sep='\t',
              encoding='utf-8-sig', index=False)


def AnalyseLocation(destination_filename):
    """Identifies the most common location for IT jobs.

    Args:
        destination_filename (str): path where statistics will be saved.
    """
    JobsPerDistrict = {'Black River': 0, 'Flacq': 0,
                       'Grand Port': 0, 'Moka': 0, 'Pamplemousses': 0,
                       'Plaine Wilhems': 0, 'Port Louis': 0,
                       'Riviere du Rempart': 0, 'Savanne': 0}
    for row in range(len(jobs_df)):
        location = jobs_df.loc[row, "location"].replace('\r\n', '',).strip()
        if location != "Mauritius" and location != "Rodrigues":
            JobsPerDistrict[location] += 1

    # Rename Plaine Wilhems to Plaines Wilhems
    # (myjob.my incorrectly wrote "Plaine Wilhems")
    JobsPerDistrict['Plaines Wilhems'] = JobsPerDistrict.pop('Plaine Wilhems')

    df = pd.DataFrame(list(JobsPerDistrict.items()),
                      columns=['Location', 'JobCount'])

    df.to_csv(destination_filename, sep='\t',
              encoding='utf-8-sig', index=False)


def filterData():
    folder = 'data/filtered/'  # folder name
    AnalyseLanguages(folder + 'LanguageData.csv')
    AnalyseDatabases(folder + 'DatabaseData.csv')
    AnalyseWebFrameworks(folder + 'WebData.csv')
    AnalyseOtherTools(folder)  # will save multiple files
    AnalyseLocation(folder + 'LocationData.csv')
    AnalyseSalary(folder + 'SalaryData.csv')


if __name__ == "__main__":
    filterData()
