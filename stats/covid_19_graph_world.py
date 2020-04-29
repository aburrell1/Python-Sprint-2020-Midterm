import matplotlib.pyplot as plt
import requests
import csv

url = "https://pkgstore.datahub.io/core/covid-19/worldwide-aggregated_json/data/8d7f2363a0c8cfd4e0c71f98cdbd0661/worldwide-aggregated_json.json"

headers = {'Accept': url}
r = requests.get(url, headers=headers)
response_dict = r.json()

#########################################################################################################
# Construct lists for the graph
#########################################################################################################
dates = [response_dict[x]['Date'] for x in range(39, len(response_dict) - 2)]
cases = [response_dict[x]['Confirmed'] for x in range(39, len(response_dict) - 2)]
deaths = [response_dict[x]['Deaths'] for x in range(39, len(response_dict) - 2)]
recoveries = [response_dict[x]['Recovered'] for x in range(39, len(response_dict) - 2)]
d_rates1 = [(response_dict[x]['Deaths']) / (response_dict[x]['Confirmed']) for x in range(39, len(response_dict) - 2)]
d_rates2 = [(response_dict[x]['Deaths']) / (response_dict[x]['Recovered']) for x in range(39, len(response_dict) - 2)]

new_data = []
for x in range(0, len(cases)):
    new_data.append([dates[x], cases[x], deaths[x], recoveries[x], d_rates1[x], d_rates2[x]])

with open('data/covid_19_world.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_data)

"""Set titles and labels"""
fig, ax = plt.subplots()
ax.set_title("COVID-19 information(deaths, recoveries, etc.) in the US from March 1st, 2020 to April 20, 2020"
             ".", fontsize=15)
ax.set_xlabel("Dates", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Accumulative Number of Cases, Deaths, Recoveries, etc.(in millions)", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=6)

"""FIRST GRAPH"""
# Infections
plt.text(40, 2500000, s='Number of Infections')
plt.plot(dates, cases, '-o')

# Deaths
plt.text(51, 30000, s='Deaths')
plt.plot(dates, deaths, '-o', c='red')

# Recoveries
plt.text(51, 600000, s='Recoveries')
plt.plot(dates, recoveries, '-o', c='orange')

# Set axis and plot the first graph
ax.axis([-1, 52, -30000, 3000000])
plt.show()

"""SECOND GRAPH(for the d_rates)"""
fig, ax = plt.subplots()
ax.set_title("COVID-19 death rates in the US from March 1st, 2020 to April 20, 2020"
             ".", fontsize=15)
ax.set_xlabel("Dates", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("death rates at certain dates", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=6)

# Plot d_rates1
plt.text(51, 0, s='d_rate1')
plt.plot(dates, d_rates1, '-o', c='yellow')

# Plot d_rates2
plt.text(51, 0.6, s='d_rate2')
plt.plot(dates, d_rates2, '-o', c='green')

plt.show()

"""Write d_rates information to the console"""

print("The d_rates work like this: if the death rate grows higher than the infection or recovery rate, the d_rate "
      "grows, otherwise it shrinks. \nIf the death rate and infection or recovery rates are similar, then the graph "
      "remains stagnant.\n"
      "d_rate1 starts out higher than d_rate2 because the number of infections starts higher than the number of "
      "recoveries. \nTherefore the ratio of deaths/infections is lower than deaths/recoveries.\n"
      "The number of infections starts out growing much faster than the number of recoveries.\n"
      "Therefore d_rate1 remains low with a small ratio. Meanwhile, d_rate2 springs up because the number of "
      "recoveries gets higher slowly whereas the death count goes up much faster.\n"
      "However, the rate of recoveries starts to grow higher than the rate of deaths and therefore d_rate2 gets smaller"
      ".\n"
      "At the end, d_rate2 remains flat because the death rate and recovery rates are similar to each other.")
