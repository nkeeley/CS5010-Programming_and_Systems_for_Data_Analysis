# File: mod4hw_scraper_keeley.py
# CS 5010
# Homework 4: Python and Web Scraper (Python version: 3)
# Nicholas Keeley, ngk3pf

### Sources used: 
# (1) https://first-web-scraper.readthedocs.io/en/latest/.
# (2) https://stackoverflow.com/questions/43617174/regex-or-replace-with-wildcard.
# (3) Drew Pearson, dp62k. Consulted about unicode translation. 
# (4) https://stackoverflow.com/questions/1207457/convert-a-unicode-string-to-a-string-in-python-containing-extra-symbols
# (5) https://realpython.com/beautiful-soup-web-scraper-python/#part-3-parse-html-code-with-beautiful-soup
# (6) https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas
# (7) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# (8) https://www.geeksforgeeks.org/adding-new-column-to-existing-dataframe-in-pandas/
# (9) https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data
# (10) https://en.wikipedia.org/wiki/World_population
# (11) https://stackoverflow.com/questions/31199710/pandas-add-row-instead-of-column


# Target: https://en.wikipedia.org/wiki/2009_swine_flu_pandemic

### Reading in packages. # Stays the same for webscrapers
import csv
import unicodedata
import requests
import re
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
import numpy


### Read in the URL and make it accessible in Python 3.
url = 'https://en.wikipedia.org/wiki/2009_swine_flu_pandemic'
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

## Select HTML data range.
soup = BeautifulSoup(html, "html.parser") # (5)
table = soup.find("table", attrs={"class":"wikitable"}) # , attrs={"class":"svelte-1f0altu"}
#print(table.prettify()) # Uncomment to show you the beautiful version of html.

## Read table rows and columns into lists. Uses nested loops: rows, then cells.
list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll("td"):
        # Clean the text to remove literals and footnotes.
        text= cell.text.replace("\n", "")
        text = re.sub("\[2..\]","",text)
        text2 = unicodedata.normalize("NFKD", text) # (3) (4)
        list_of_cells.append(text2) # Add each cell to a list.
    list_of_rows.append(list_of_cells) # Add each list to a list of "rows"

## Push to file.
outfile = open("./FluStats.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Date", "World Pop.", "Subtype", "Reproduction Number", 
                    "Infected (Est.)", "Deaths Worldwide", "Case Fatality Rate",
                    "Pandemic Severity"])
writer.writerows(list_of_rows)

## Transform csv into a Pandas data frame and clean data.
data=pd.read_csv("./Flustats.csv") #(7)
# Add missing column. 
data.insert(0, "Name", ["1889-1990 Flu Pandemic", "1918 Flu", "Asian Flu", "Hong Kong Flu",
                        "2009 Flu Pandemic", "", ""]) # (8))
#print(data.loc[:, ["Name"]])

## Trim to remove NaN and yearly flu stats.
data2=data[0:5]
#print(data2.tail())

## Turn data into information: Conservative worldwide death tolls per year.
data2.insert(9, "Conservative Worldwide Death Toll (in thousands)", [1000,
                                                                     17000, 
                                                                     1000, 
                                                                     1000, 
                                                                     151.7])
data2.insert(10, "Duration (in years)",[2, 3, 2, 2, 2])
deaths_per_year =  data2["Conservative Worldwide Death Toll (in thousands)"]/data2["Duration (in years)"]
# print(deaths_per_year)
data2.insert(11, "Conservative Worldwide Death Toll per Year (in thousands)", deaths_per_year)
#print(data2.columns)

## Add COVID-19 data for last 6 months. #(9) # (10) 
data2.loc[len(data2)] = ["COVID-19", "2019-TBD", "7.8 billion", "Coronavirus", "TBD",
                      "15.6 million", "636K", ">4%", "TBD", 636, 0.5, 1272] # (11)
#print(data2)

## Visualize through bar graphs.
plt.bar(data2["Name"], data2["Conservative Worldwide Death Toll per Year (in thousands)"])


