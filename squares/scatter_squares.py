import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# s为点的尺寸 edgecolors为数据点的轮廓
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
"""要了解pyplot中所有的颜色映射，请访问http://matplotlib.org/，单击Examples，向下滚动
到Color Examples，再单击colormaps_reference。"""
# 设置图标标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# plt.show()
# bbox_inches='tight'裁剪到空白区域
plt.savefig('squares_plot.png', bbox_inches='tight')