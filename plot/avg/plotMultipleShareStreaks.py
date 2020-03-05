# ---------- IMPORT ------------
import logging
import json
import datetime
import matplotlib
import matplotlib.pyplot as plt
# ------------------------------


# ---------- INPUT -------------
path_source = "C:/Users/Lukas/Desktop/streakShareValues.json"
# ------------------------------


# ---------- OUTPUT ------------

# ------------------------------


# ---------- CONFIG ------------
c = ["#17719B", "#32A875", "#E5C35E"]
# ------------------------------


# ---------- INITIAL -----------
logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
datetimeFormat = "%Y-%m-%d"
# ------------------------------



# ------------- 3 years -------------
with open(path_source, "r") as fp:
    plotdata = json.load(fp)

i = 0
for t in plotdata:
    values = []
    list_of_datetimes = []
    for entry in plotdata[t]:
        values.append(plotdata[t][entry])
        list_of_datetimes.append(datetime.datetime.strptime(entry, datetimeFormat).date())
    dates = matplotlib.dates.date2num(list_of_datetimes)
    matplotlib.pyplot.plot_date(dates, values, '-', label="t=" + str(t), color=c[i])
    i += 1

plt.xlabel("Time", fontsize=13)
plt.ylabel("Share of users having a streak of length > t days", fontsize=13)

plt.axvline(x=datetime.datetime.strptime("2016-05-19", datetimeFormat).date(), color='#D3685D', label="Design change")
plt.axvline(x=datetime.datetime.strptime("2016-12-25", datetimeFormat).date(), color='#8C8C8C', ls=":", label="Christmas")
plt.axvline(x=datetime.datetime.strptime("2017-12-25", datetimeFormat).date(), color='#8C8C8C', ls=":")
plt.axvline(x=datetime.datetime.strptime("2015-12-25", datetimeFormat).date(), color='#8C8C8C', ls=":")
plt.axvline(x=datetime.datetime.strptime("2016-07-04", datetimeFormat).date(), color="#8C8C8C", ls=":", label="Independence Day")
plt.axvline(x=datetime.datetime.strptime("2017-07-04", datetimeFormat).date(), color="#8C8C8C", ls=":")
plt.axvline(x=datetime.datetime.strptime("2015-07-04", datetimeFormat).date(), color="#8C8C8C", ls=":")

plt.axvline(x=datetime.datetime.strptime("2015-03-26", datetimeFormat).date(), color='#8C8C8C', ls="--", label="GitHub Server DDoS-Attack (2015)")
plt.axvline(x=datetime.datetime.strptime("2016-12-06", datetimeFormat).date(), color='#8C8C8C', ls="--", label="GitHub Major Service Outage (2016)")


plt.legend(fontsize=11)
plt.show()