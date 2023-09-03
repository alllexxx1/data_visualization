import csv
from datetime import datetime
from matplotlib import pyplot as plt


filepath = ('/home/aleksei/projects/data_visualization'
            '/data/new_york_weather_2023.csv')
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, snow = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            s = row[4]
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            snow.append(s)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, snow, c='blue', alpha=0.5)

title = 'The amount of snow in 2023\nNew York'
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Snow', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
