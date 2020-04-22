#from plotly.graph_objs import Bar, Layout
from plotly import offline
import pandas
import stats
import plotly.express as px

import matplotlib.pyplot as plt
import csv


filename = 'data/covid_19.csv'

# Got the information on the markers for the line graph here:
# https://stackoverflow.com/questions/8409095/matplotlib-set-markers-for-individual-points-on-a-line

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    number_of_infections = []
    deaths = []
    recoveries = []

    for row in reader:
        dates.append(row[0])
        number_of_infections.append(float(row[1]))
        deaths.append(float(row[2]))
        recoveries.append(float(row[3]))

fig, ax = plt.subplots()
#ax.plot(dates, number_of_infections, c="red", alpha=0.5)

# Set title and labels.
ax.set_title("COVID-19 information(including deaths, recoveries, etc.) in the US from March 1st, 2020 to April 20, 2020"
             ".", fontsize=15)
ax.set_xlabel("Dates", fontsize=5)
fig.autofmt_xdate()
ax.set_ylabel("Accumulative Number of Cases, Deaths, Recoveries, etc.", fontsize=5)
ax.tick_params(axis="both", which="major", labelsize=6)

# Plot all rows
plt.text(33, 750000, s='Number of Infections')
plt.plot(dates, number_of_infections, '-o')

plt.text(50, 1000, s='Deaths')
plt.plot(dates, deaths, '-o', c='red')

plt.text(50, 95000, s='Recoveries')
plt.plot(dates, recoveries, '-o', c='orange')


# Set axis
ax.axis([-1, 52, -30000, 800000])

# for i_x, i_y in zip(dates, number_of_infections):
#     plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

#plt.plot(dates, deaths, '-o')

plt.show()