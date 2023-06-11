import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 14

# 定义文件名变量
file_name = 'load_latency'
# file_name = 'run_latency'

# 从csv文件中读取数据
with open(f'{file_name}.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    data = []
    for row in reader:
        data.append(row)

# 将数据转换为列表
labels = [row[0] for row in data]
values1 = [float(row[1]) for row in data]
values2 = [float(row[2]) for row in data]
values3 = [float(row[3]) for row in data]
values4 = [float(row[4]) for row in data]

# 绘图
x = range(len(labels))
width = 0.15
fig, ax = plt.subplots(dpi=200)
rects1 = ax.bar(x, values1, width, label='SepHash')
rects2 = ax.bar([i + width for i in x], values2, width, label='RACE')
rects3 = ax.bar([i + 2*width for i in x], values3, width, label='Plush')
rects4 = ax.bar([i + 3*width for i in x], values4, width, label='Clevel')

# 设置图表参数
ax.set_ylabel('Time (ns)')
ax.set_xlabel('Data Size')
ax.set_xticks([i + 2*width for i in x])
ax.set_xticklabels(labels)
ax.legend()

# 保存图表为pdf
plt.savefig(f'{file_name}.pdf', format='pdf')

# 显示图表
plt.show()