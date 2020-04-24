import matplotlib.pyplot as plt
import csv

# READ THIS
###################################################################################################################
# The information regarding infections, deaths, and recoveries opens when you click run.
# The second graph contains the d_rates graphs. You have to close the first graph in order for this one to open.
# When the second graph is closed, then the explanation of the d_rates will show up in the console.
###################################################################################################################

# SOURCES
###################################################################################################################
# https://covidusa.net/?autorefresh=1
# https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html
###################################################################################################################


filename = 'data/covid_19.csv'

"""Process the csv file and extract information to use for the graph."""
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates = []
    number_of_infections = []
    deaths = []
    recoveries = []
    d_rates1 = []
    d_rates2 = []




    # Rewrite the file using the contents in this list. This is the best option I have right now. I do not know how
    # to write to specific columns in a csv file.
    new_data = []

    # In the rewritten file, write the header row first.
    new_data.append(header_row)

    # Append the headers "d_rate1" and "d_rate2".
    new_data[0][4] = "d_rate1"
    new_data[0][5] = "d_rate2"

    for row in reader:
        # Append the data containing everything including the two d_rates.
        new_data.append([row[0], row[1], row[2], row[3], float(row[2]) / float(row[1]),
                         (float(row[2]) / float(row[3]))])

        # Append the data from the file into the lists to use for the graphs.
        dates.append(row[0])
        number_of_infections.append(float(row[1]))
        deaths.append(float(row[2]))
        recoveries.append(float(row[3]))
        d_rates1.append(float(row[2]) / float(row[1]))
        d_rates2.append(float(row[2]) / float(row[3]))

print(header_row[4])

# Write the new data that includes the d_rates into the file.
with open('data/covid_19.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_data)


"""Set titles and labels"""

fig, ax = plt.subplots()
ax.set_title("COVID-19 information(including deaths, recoveries, etc.) in the US from March 1st, 2020 to April 20, 2020"
             ".", fontsize=15)
ax.set_xlabel("Dates", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Accumulative Number of Cases, Deaths, Recoveries, etc.", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=6)

"""FIRST GRAPH"""
# Infections
plt.text(40, 750000, s='Number of Infections')
plt.plot(dates, number_of_infections, '-o')

# Deaths
plt.text(51, 30000, s='Deaths')
plt.plot(dates, deaths, '-o', c='red')

# Recoveries
plt.text(51, 95000, s='Recoveries')
plt.plot(dates, recoveries, '-o', c='orange')

# Set axis and plot the first graph
ax.axis([-1, 52, -30000, 800000])
plt.show()


"""SECOND GRAPH(for the d_rates)"""
fig, ax = plt.subplots()
ax.set_title("COVID-19 death rates in the US from March 1st, 2020 to April 20, 2020"
             ".", fontsize=15)
ax.set_xlabel("Dates", fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("death rates at certain dates", fontsize=10)
ax.tick_params(axis="both", which="major", labelsize=6)

#Plot d_rates1
plt.text(51, 0, s='d_rate1')
plt.plot(dates, d_rates1, '-o', c='yellow')

#Plot d_rates2
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