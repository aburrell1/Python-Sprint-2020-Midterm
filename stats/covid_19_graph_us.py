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

    for row in reader:
        dates.append(row[0])
        number_of_infections.append(float(row[1]))
        deaths.append(float(row[2]))

# data = [{
#     'type': 'bar',
#     'x': dates,
#     'y': number_of_infections,
#     'marker': {
#         'color': 'rgb(255, 0, 0)',
#         'line': {'width': 1.5, 'color': 'rgb(10, 10, 10)'},
#     },
#     'opacity': 0.5
# }]
#
# my_layout = Layout(title='COVID-19 deaths in the US from March 1st, 2020 to April 20, 2020.')
# my_layout = {
#     'title': 'COVID-19 deaths in the US from March 1st, 2020 to April 20, 2020.',
#     'xaxis': {'title': 'Dates'},
#     'yaxis': {'title': 'Accumulative Number of Cases'},
# }
#
# my_layout = Layout(title='World Fires')
# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='world_fires_1_day.html')

fig, ax = plt.subplots()
y_values = [element for element in number_of_infections]
#ax.plot(dates, number_of_infections, c="red", alpha=0.5)

ax.set_title("COVID-19 information(including deaths, recoveries, etc.) in the US from March 1st, 2020 to April 20, 2020.", fontsize=25)
ax.set_xlabel("Dates", fontsize=5)
fig.autofmt_xdate()
ax.set_ylabel("Accumulative Number of Cases, Deaths, Recoveries, etc.", fontsize=5)
ax.tick_params(axis="both", which="major", labelsize=6)
print(number_of_infections)
plt.plot(dates, number_of_infections, '-o')
plt.plot(dates, deaths, '-o', c='red')
ax.axis([-1, 52, -30000, 800000])

# for i_x, i_y in zip(dates, number_of_infections):
#     plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

#plt.plot(dates, deaths, '-o')

plt.show()