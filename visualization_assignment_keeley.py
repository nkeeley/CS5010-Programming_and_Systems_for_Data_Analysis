# File: visualization_assignment_keeley.py
# CS 5010
# Module 11 Assignment (Python version: 3)
# Nicholas Keeley, ngk3pf

## Read in the data
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tips.csv")
df2=df.groupby("day").sum()


## Line plot.
fig=plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(df2["tip"], 'k--', label="Tips") # green dashed line
plt.ylabel('Tip Amount')
plt.title('Tip Sum By Day')
plt.legend()
plt.close("all")


## Bar plot.

plt.bar(df["day"], df["total_bill"])
plt.ylabel('Total Bill')
plt.title('Total Bill By Day')
plt.close("all")



## Histogram.

plt.hist(df["total_bill"])
plt.ylabel('Frequency')
plt.xlabel("Total Bill")
plt.title('Total Bill Frequency')
plt.close("all")



## Scatter plot.

plt.scatter(df["total_bill"], df["tip"])
plt.ylabel('Tip')
plt.xlabel("Total Bill")
plt.title('Tip Against Total Bill')
plt.close("all")

## Boxplot.

plt.boxplot(df["total_bill"])
plt.ylabel('Total Bill')
plt.title('Total Bill Boxplot')

