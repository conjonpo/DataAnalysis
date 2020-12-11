# Data Analysis

Author, Conner Pohlsander

## Overview

## Development Environment

* Python 3.8.2
* Visual Studio Code
* Python extension for VS Code
* Pandas package for Python
* Seaborn package for Python

## Execution

First, the pandas and seaborn packages for Python need to be downloaded. Add the following code to activate the packages:

```
import pandas as pd
import seaborn as sns
```

The next step is to find and add data in csv format. I used [this data](https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018). The code for reading in this data uses the pandas package and looks like this:

```
teams = pd.read_csv("CFBeattendance.csv", encoding = "ISO-8859-1")
```

I had to specify encoding since my data had characters not normally recognized.

## Helpful Links

* [https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018](https://www.kaggle.com/jeffgallini/college-football-attendance-2000-to-2018)
* [https://pandas.pydata.org/docs/getting_started/overview.html](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Stack Overflow](https://stackoverflow.com/)