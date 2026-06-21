from pathlib import Path

import csv

import matplotlib.pyplot as plt, matplotlib.dates as mdates

from datetime import datetime

path = Path("weather_data/death_valley_2021_simple.csv")

lines = path.read_text(encoding = 'utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

for index, value in enumerate(header_row):
    print(index, value)

highs, lows, dates = [],[],[]
for row in reader:
    try:
        high = int(row[3])
        low = int(row[4])
        date = datetime.strptime(row[2],'%Y-%m-%d')

    except ValueError:
        print(f"Missing data  for {date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(dates,highs,color = 'red', alpha = 0.5)
ax.plot(dates,lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

ax.set_title("Daily High and Lows Temperatures, 2021", fontsize = 14)
ax.set_xlabel("Dates", fontsize = 10)
ax.set_ylabel("Temperature (F)", fontsize = 10)
ax.tick_params(labelsize = 8)
fig.autofmt_xdate()

plt.show()



