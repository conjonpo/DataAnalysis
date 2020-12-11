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

#print(nba3[["firstName", "lastName", "year", "tmID", "points", "pos", "threeMade"]].sort_values("threeMade", ascending=False).head(20))

#teams2 = teams["Fill Rate", "Conference", "Year"]

#print(teams2) 

teams_grouped_year = teams[["Fill Rate", "Year"]].groupby("Year").mean()

teams_grouped_year.rename(columns={0 : 'Year', 1 : 'Fill Rate'}, inplace=True)

print(teams_grouped_year)

#sns.lineplot(data=mean2, x="Conference", y="Fill Rate").set_title("Average Fill Rate per Year")
#plt.show()