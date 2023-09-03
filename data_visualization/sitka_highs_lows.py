import csv
from datetime import datetime
from matplotlib import pyplot as plt


def convert_to_celsius(fahr_temp: str) -> int:
    celsius_temp = (5 / 9) * (float(fahr_temp) - 32)
    return int(celsius_temp)


filepath = ('/home/aleksei/projects/data_visualization'
            '/data/sitka_weather_2021_simple.csv')
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, dates, lows = [], [], []
    for row in reader:
        high = convert_to_celsius(row[4])
        highs.append(high)
        date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(date)
        low = convert_to_celsius((row[5]))
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title('Daily high and low temperatures - 2021', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
