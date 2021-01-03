import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = '../data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 获取日期、最高气温和最低气温
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # 要安装datetime
            current_data = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])  # 数据读出来是字符串
            low = int(row[3])
        except ValueError:
            print(current_data, 'missing data')
        else:
            dates.append(current_data)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)  # alpha为透明度
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
# plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()