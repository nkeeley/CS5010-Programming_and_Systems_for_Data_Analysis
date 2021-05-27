# File: read_dataMod.py
# CS 5010
# Learning Python (Python version: 3)

# Demonstrating use of pandas using comScore Media Metrix data set
# ( Key_Measures_December_2013_Mod.csv )

from numpy import *
import pandas as pd

# For output purposes to show all columns:
pd.set_option('display.max_columns', None)

# One of the parameters is "skiprows'. So we find the rows to skip
# Skipping first 7 rows (which is range(7)=0 to 6) 
# and rows 6942 to 6979 (which is range (6941,6979) due to rows starting at #0)
beginningRows = list(range(7))
endingRows = list(range(6941,6979))
skips = beginningRows + endingRows

# One of the parameters is "usecols". Used to find the columns of interest.
useTheseCols = list(range(0,13)) # Grabbing columns including the first

# header=0 means that we assign the headers to first row we read (not including the skipped)
# Read the csv file:
df = pd.read_csv('Key_Measures_December_2013_Mod.csv',skiprows=skips,usecols=useTheseCols,header=0,encoding = "ISO-8859-1")

print("  *** Using file: Key_Measures_December_2013_Mod.csv ***")

# Print the first 5 data points (using "head")
print("\n****************")
print('*** The first 5 data points\n',df.head(6))




# Print the last 5 data points (using "tail")
print("\n****************", end='')
print('\n*** The last 5 data points\n',df.tail(5))

# Print the column headers
print('\n****************')
print('*** The column headers\n',df.columns)

# Notice one column doesn't have a header. Can rename to 'Webpage Reference'
df.rename(columns={'Unnamed: 0' : 'Webpage Reference'},inplace=True)

print("=====================================")
print(df.columns)

# Renaming columns is quite easy to do 
# (Can also rename multiple columns at a time if desired - not shown here)
df.rename(columns={'Category' : 'CATEGORY'},inplace=True)

# Display updated column headers
print("\n****************", end='')
print('\n*** Changed column headers:\n',df.columns)


#print('\nWebpage Reference Column (first 10 results):\n',df['Webpage Reference'])
print("\n****************", end='')
print('\nAverage Daily Visitors (first 10):\n',df['Average Daily Visitors (000)'].head(10))

# Running some queries:
# Suppose we want to find "Total Visits" greater than 100
print("\n****************", end='')
print('\n**** Total Visits > 100 (first 25 results):\n',df[df['Total Visits (000)'] < 100].head(25))

# Suppose we want to find total Visits greater than 100000 and  Visits Per Visitor > 50.
print("\n****************", end='')
print('\n**** Visits greater than 100000 and Average Visits Per Visitor > 50:')
print(df[(df['Total Visits (000)'] > 100000) & (df['Average Visits per Visitor'] > 50)])


