## Dependencies ##
```
Python : 3.9.7
Panda : 1.3.3
BeautifulSoup : 4.10.0
MatPlotLib : 3.4.3
Plotly : 5.8.0
```


## Usage ## 
> ⚠️For the time being (May 2022), myjob.mu does not have any policy against web scraping. This may change in the future so use `DataMiner.py` at your own risk.

> ⚠️`DataMiner.py` may not work if myjob.mu changes the format its website.

1. Run `WebScraping()` function in `DataMiner.py` to scrape data from myjob.mu and update the list of jobs in `RawScrapedData.csv`
2. Run `main()` function in `DataAnalyser.py` to extract relevant data from the updated `RawScrapedData.csv`. Extracted data will be saved to a new folder `FilteredData`.
3. Run  `main()` function in `DataVisualiser.py` to create charts from the filtered data. Charts will be saved to a new folder `FilteredData`.

Your file directory will look like this :
```
project
│   DataAnalyser.py
|   DataMiner.py
|   DataVisualiser.py
|   mauritius-districts-geojson
|   RawScrapedData.csv
|   choropleth-map-plotly-python.html
|
│
└───FilteredData
│   │   CloudData.csv
│   │   DatabaseData.csv
│   |   ...
│    
│   
└───Charts
    │   CloudChart.png
    │   DatabaseChart.png
    |   ...
```
## DataVisualiser.py ##

Available data visualisation techniques :
- Horizontal barchart
- Pie chart
- Donut chart
- Choropleth map
- Lollipop chart 
### Improving quality of saved images ###

In `DataAnalyser.py`, when saving charts, change the file extension to .pdf to save higher quality images.

```python
    HorizontalBarChart(source_path + "DatabaseData.csv",
                       destination_path + "DatabaseChart", '#5FE916', "Databases.pdf") # pdf file extension
```
