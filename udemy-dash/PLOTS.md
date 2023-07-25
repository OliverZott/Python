# Plots Summary

## Scatterplot

- Compare two variables of one dataset

## Lineplot

- Used to show trend over time (aka **time series**)
- basically scatterplot with lines

## Barplot

- barplot shows **categorical data**
- height, length proportional to the values they represent
- barplot is a good choice when you want to show how some quantity varies among some discrete set of items
- x axis is categorical (category), y axis is numerical (value)
- y axis can be **aggregation**: count, sum, average, median, etc.

Reminder:

- categorical:
    e.g. sex, smoker, day
- continuous:
    e.g. total_bill, tip, size

## Bubbleplot

- like scatter plot ("Streudiagramm")
- additionally: size of marker is proportional to a third variable  
- additional variable is represented by the color of the marker (based on category)

## Boxplot

- are used to show the distribution of numerical data and skewness through displaying the data quartiles (or percentiles) and averages.
- are used to detect outliers in data.
- we can split data based on categorical data and compare continuous data between feature.

## Boxplot basics

- IQR (interquantil range) = Q3 - Q1
- Whiskers show max and min values (data range)
- Ausreißer = 1.5 * IQR (lower or higher) are shownm as single points above Whiskers

## Histogram

- like barplot but for continuous/numerical values instead categroical
- x axis is numerical (value), y axis is count
- is a type of bar chart that shows the frequency or number of values compared to a set of value ranges.
  - intervals and count per interval (**Bins**)
- is a great way to display **continuous data**

## Distplot

- is a combination of the histogram with the **kernel density estimate** (KDE)
- KDE is a non-parametric way to estimate the probability density function of a random variable
- KDE is a smoothed version of the histogram
