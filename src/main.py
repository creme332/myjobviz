#!venv/bin/python3

from miner import scrapeWebsite
from analyser import filterData
from visualiser import createVisualisations

if __name__ == "__main__":
    scrapeWebsite()
    filterData()
    createVisualisations()