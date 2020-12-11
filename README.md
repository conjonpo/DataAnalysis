# Data Analysis

Author, Conner Pohlsander

## Overview

I have had an interest in college football for most of my life. I especially like the data side of sports, which is my focus for this analysis. For this analysis, I will analyze data pertaining to attendance for football games over a time period from 2000-2018 for 63 different teams in college football. I have three questions that I am looking to answer:
* **Which universities struggle the least to fill their football stadiums and which struggle the most?**
* **Which college football conferences do the best with filling their stadiums?**
* **Has attendance at games been declining across the sport?**

## Development Environment

* Python 3.8.2
* Visual Studio Code
* Python extension for VS Code
* Pandas package for Python
* Seaborn package for Python

## Execution

### Getting Started

First, the pandas and seaborn packages for Python need to be downloaded. Add the following code to activate the packages:

```
import pandas as pd
import seaborn as sns
```

The next step is to find and add data in csv format. I used [this data](https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018). The code for reading in this data uses the pandas package and looks like this:

```
teams = pd.read_csv("CFBeattendance.csv", encoding = "ISO-8859-1")
```

I had to specify encoding since my data had characters not normally recognized. With the data loaded in, I could move on to answering my questions.


## Helpful Links

* [https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018](https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018)
* [https://pandas.pydata.org/docs/getting_started/overview.html](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Stack Overflow](https://stackoverflow.com/)