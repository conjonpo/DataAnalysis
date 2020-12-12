import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

teams = pd.read_csv("CFBeattendance.csv", encoding = "ISO-8859-1")

mean = teams[["Team", "Fill Rate"]].groupby("Team").mean()

print(f"Mean: {mean}")

print(mean[["Fill Rate"]].sort_values("Fill Rate", ascending=False).head(20))

print(mean[["Fill Rate"]].sort_values("Fill Rate", ascending=True).head(20))

mean2 = teams[["Conference", "Fill Rate"]].groupby("Conference").mean()

print(mean2[["Fill Rate"]].sort_values("Fill Rate", ascending=False).head(20))

teams_grouped_year = teams[["Fill Rate", "Year"]].groupby("Year").mean()

print(teams_grouped_year)

yearly = pd.read_csv("CFBYearlyAttendance.csv")

sns.lineplot(data=yearly, x="Year", y="Fill_Rate").set_title("Average Fill Rate per Year")
plt.show()