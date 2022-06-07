# -*- coding: utf-8 -*-
"""
Created on Fri May 6 2022
Python Version : 3.9.7
Panda version : 1.3.3
MatPlotLib : 3.4.3
plotly Version: 5.8.0
Summary : Visualise data from FilteredData and save results to Charts folder.
@author: me
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'  # to show geojson map in web browser

data_source_filename = 'RawScrapedData.csv'
jobs_df = pd.read_csv(data_source_filename)
jobs_df.drop_duplicates(
    subset=None, keep='first', inplace=False)  # drop duplicates

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 500)


def HorizontalLollipopChart(source_filename, destination_filename):
    # using data from csv file
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns

    # my_labels = df[column_headings[0]].tolist()
    # my_data = df[column_headings[1]].tolist()

    # when using data from dictionary
    # df = pd.DataFrame(list(dictionary.items()), columns=['Name', 'Value'])

    # Reorder it based on the values:
    ordered_df = df.sort_values(by=column_headings[1])  # VARIABLE
    my_range = range(1, len(df.index)+1)
    plt.style.use('default')

    # Horizontal version
    plt.hlines(y=my_range, xmin=0,
               xmax=ordered_df[column_headings[1]], color='skyblue')
    plt.plot(ordered_df[column_headings[1]], my_range, "D")
    plt.yticks(my_range, ordered_df[column_headings[0]])

    # plt.savefig(destination_filename, bbox_inches='tight')
    plt.show()
    plt.close()


def HorizontalBarChart(source_filename, destination_filename, my_color):
    # =============================================================================
    #     for key in list(dictionary):
    #         if dictionary[key] == 0:
    #             dictionary.pop(key, None)
    # =============================================================================
    df = pd.read_csv(source_filename, sep='\t')
    df = df.sort_values(by=['Frequency'])

    column_headings = df.columns

    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()

# =============================================================================
#     # when reading from dictionary
#     my_labels = list(dictionary.keys())
#     my_data = list(dictionary.values())
# =============================================================================

    # colors = ['red', 'yellow', 'green', 'blue', 'orange', 'black']
    cmap = plt.cm.tab10
    # colors = cmap(np.arange(len(my_labels)) % cmap.N)
    plt.style.use('ggplot')

    plt.barh(my_labels, my_data, color=my_color)
    # plt.title('Programming languages')
    plt.ylabel(column_headings[0])  # VARIABLE
    plt.xlabel(column_headings[1])

    plt.show()
    # plt.savefig(destination_filename, bbox_inches='tight')
    plt.close()


def VerticalBarChart(dictionary, filename):
    # filter out data which have a count of 0
    for key in list(dictionary):
        if dictionary[key] == 0:
            dictionary.pop(key, None)

    plt.bar(range(len(dictionary)), dictionary.values(),
            align='center', width=0.3)
    plt.xticks(range(len(dictionary)), dictionary.keys())

    plt.savefig(filename, bbox_inches='tight')
    plt.close()


def PieChart(source_filename, destination_filename, my_color):
    # =============================================================================
    #     # filter out languages which have not been used at all
    #     for lang in list(languages):
    #         if languages[lang] == 0:
    #             languages.pop(lang, None)
    #
    #     languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    #     x, y = zip(*languages)  # unpack a list of pairs into two tuples
    # =============================================================================

    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns

    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()
    # create a figure and set different background
    fig = plt.figure()
    # fig.patch.set_facecolor('black')

    # Change color of text
    plt.rcParams['text.color'] = 'black'

    # Create a circle at the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='grey')

    # Pieplot + circle on it
    plt.pie(my_data, labels=my_labels, shadow=True, autopct='%1.1f%%')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.legend()
    plt.show()
    # plt.savefig(destination_filename)
    plt.close()


def donutChart(source_filename, destination_path):
    # https://medium.com/@krishnakummar/donut-chart-with-python-matplotlib-d411033c960b
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns
    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    # explode = (1, 0, 0)  # explode a slice if required.
    # len(explode) = number of rows in df. Then add explode = explode below

    plt.pie(my_data, labels=my_labels, colors=colors,
            autopct='%1.1f%%', shadow=True)

    # draw a circle at the center of pie to make it look like a donut
    centre_circle = plt.Circle(
        (0, 0), 0.75, color='black', fc='white', linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()


def CreateMap(source_path, destination_path):

    districts = json.load(open("mauritius-districts-geojson.json", 'r'))
    df = pd.read_csv(source_path, sep='\t')

    # create a log scale to deal with outliers in JobCount
    # get rid of 0s in column (log 0 invalid)
    df["JobCount"].replace(0, 1, inplace=True)
    df['JobCountScale'] = np.log10(df['JobCount'])

    fig = px.choropleth(df, geojson=districts,
                        featureidkey='properties.name_1',
                        locations='Location',  # column in dataframe which contains districts names
                        color='JobCountScale',  # data from this column in dataframe is plotted
                        color_continuous_scale="turbo",  # turbo or blackbody
                        range_color=[0, max(df['JobCountScale'])],
                        labels={"Value": "Count"}
                        )
    fig.update_geos(fitbounds="locations")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    fig.write_image(destination_path + ".svg")  # .svg or .pdf

    # fig.show()


def main():
    source_path = 'FilteredData/'  # folder containing filtered data
    destination_path = 'Charts/'  # folder to store charts

    # CreateMap(source_path + "LocationData.csv", destination_path + "JobCountMap")

    HorizontalBarChart(source_path + "CloudData.csv",
                       destination_path + "CloudChart", 'blue')
    HorizontalBarChart(source_path + "DatabaseData.csv",
                       destination_path + "DatabaseChart", 'green')
    HorizontalBarChart(source_path + "LanguageData.csv",
                       destination_path + "LanguageChart", 'orange')
    HorizontalBarChart(source_path + "LibrariesData.csv",
                       destination_path + "LibrariesChart", 'black')
    HorizontalBarChart(source_path + "OSData.csv",
                       destination_path + "OSChart", 'red')
    HorizontalBarChart(source_path + "ToolsData.csv",
                       destination_path + "ToolsChart", 'purple')
    HorizontalBarChart(source_path + "WebData.csv",
                       destination_path + "WebChart", 'skyblue')

    # add explanation for percentage in donut chart
    # donutChart(source_path + "OSData.csv", destination_path + "OSChart")

    # HorizontalBarChart(source_path + "", destination_path + "OSData.csv", "")

    # PieChart(source_path + "OSData.csv", destination_path + "")
    # donutChart(source_path + "WebData.csv", destination_path + "")
    # PieChart(source_path + "OSData.csv", destination_path + "")


# main()
# PieChart('FilteredData/OSData.csv', '', 'red')
