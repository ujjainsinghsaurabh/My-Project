from pathlib import Path

import csv

from datetime import datetime

import matplotlib.pyplot as plt,  matplotlib.dates as mdates

path = Path('weather_data/sitka_weather_07-2021_simple.csv')

lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

highs = []
dates = []

for row in reader:
    high = int(row[4])
    date = datetime.strptime(row[2], '%Y-%m-%d')
    highs.append(high)
    dates.append(date)

print(highs)

plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates,highs,color = 'red')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

ax.set_title("Daily High Temperatures, July 2021",fontsize = 14)
ax.set_xlabel("", fontsize = 10)
ax.set_ylabel("Temperature (F)", fontsize = 10)
ax.tick_params(labelsize = 8)
fig.autofmt_xdate()

plt.show()
