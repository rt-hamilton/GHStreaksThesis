# ---------- IMPORT ------------
import logging
import json
import datetime
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import colorConverter as cc
import numpy as np
# ------------------------------


# ---------- INPUT -------------
path_source = "C:/Users/Lukas/Desktop/streakSurvivalRatesMIN15.json"
# ------------------------------


# ---------- OUTPUT ------------

# ------------------------------


# ---------- CONFIG ------------

# ------------------------------


# ---------- INITIAL -----------
logging.basicConfig(format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)
datetimeFormat = "%Y-%m-%d"
list_of_datetimes = []
values = []
ub = []
lb = []
# ------------------------------



logging.info("Accessing plot data ...")
with open(path_source, "r") as fp:
    plotdata = json.load(fp)

for entry in plotdata:
    list_of_datetimes.append(datetime.datetime.strptime(entry, datetimeFormat).date())
    values.append(plotdata[entry]["r"])
    lb.append(plotdata[entry]["a"])
    ub.append(plotdata[entry]["b"])

dates = matplotlib.dates.date2num(list_of_datetimes)
logging.info("Done. (1/2)")


logging.info("Creating plot ...")

matplotlib.pyplot.plot_date(dates, values, '-')
#matplotlib.pyplot.plot_date(dates, lb, '-')
#matplotlib.pyplot.plot_date(dates, ub, '-')
plt.axvline(x=datetime.datetime.strptime("2016-05-19", datetimeFormat).date(), color='r')
plt.xlabel("Time")
plt.ylabel("Streak survival rate")
plt.show()


logging.info("Done. (2/2)")