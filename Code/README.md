### Dependencies ###
```
Python : 3.9.7
Panda : 1.3.3
BeautifulSoup : 4.10.0
MatPlotLib : 3.4.3
Plotly : 5.8.0
```


### Order of execution ### 
1. Run `DataMiner.py` to scrape data from myjob.mu and update the list of jobs in `RawScrapedData.csv`
2. Run `DataAnalyser.py` to extract relevant data from the updated `RawScrapedData.csv`
3. Run `DataVisualiser.py` to create charts from the filtered data.

> ⚠️For the time being (May 2022), myjob.mu does not have any policy against web scraping. This may change in the future so use `DataMiner.py` at your own risk.

