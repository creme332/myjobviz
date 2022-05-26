# -*- coding: utf-8 -*-
"""
Created on Fri May 6 2022
Python Version : 3.9.7
Panda version : 1.3.3
Summary : Create charts to visualise filtered job data from data.csv.
@author: me
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

data_source_filename = 'TESTING.csv'
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


def HorizontalBarChart(source_filename, destination_filename):
    # =============================================================================
    #     for key in list(dictionary):
    #         if dictionary[key] == 0:
    #             dictionary.pop(key, None)
    # =============================================================================
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns

    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()

# =============================================================================
#     # when reading from dictionary
#     my_labels = list(dictionary.keys())
#     my_data = list(dictionary.values())
# =============================================================================

    #colours = ['red', 'yellow', 'green', 'blue', 'orange', 'black']
    cmap = plt.cm.tab10
    colors = cmap(np.arange(len(my_labels)) % cmap.N)
    # plt.style.use('ggplot')

    plt.barh(my_labels, my_data, color=colors)
    # plt.title('Programming languages')
    plt.ylabel('Language')  # VARIABLE
    plt.xlabel('Frequency')

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


def PieChart(source_filename, destination_filename):
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
    fig.patch.set_facecolor('black')

    # Change color of text
    plt.rcParams['text.color'] = 'white'

    # Create a circle at the center of the plot
    my_circle = plt.Circle((0, 0), 0.7, color='black')

    # Pieplot + circle on it
    plt.pie(my_data, labels=my_labels, shadow=True, autopct='%1.1f%%')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.legend()
    plt.show()
    # plt.savefig(destination_filename)
    plt.close()


def donutChart(source_filename):
    # https://medium.com/@krishnakummar/donut-chart-with-python-matplotlib-d411033c960b
    df = pd.read_csv(source_filename, sep='\t')
    column_headings = df.columns
    my_labels = df[column_headings[0]].tolist()
    my_data = df[column_headings[1]].tolist()

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    #explode = (1, 0, 0)  # explode a slice if required.
    # len(explode) = number of rows in df. Then add explode = explode below

    plt.pie(my_data,labels=my_labels, colors=colors,
            autopct='%1.1f%%', shadow=True)

    # draw a circle at the center of pie to make it look like a donut
    centre_circle = plt.Circle(
        (0, 0), 0.75, color='black', fc='white', linewidth=1.25)
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.show()


# HorizontalBarChart("OSData.csv", "")
# PieChart("OSData.csv", "")
# HorizontalBarChart("OSData.csv", "")
donutChart("OSData.csv")
# PieChart("OSData.csv", "")
