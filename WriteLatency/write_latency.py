import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 定义文件名变量
# file_name = 'load_latency'
file_name = 'run_latency'

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
plt.figure(figsize=(10, 5.8))
x = range(len(labels))
width = 0.15
plt.bar(x, values1, width, label='SepHash')
plt.bar([i + width for i in x], values2, width, label='RACE')
plt.bar([i + 2*width for i in x], values3, width, label='Plush')
plt.bar([i + 3*width for i in x], values4, width, label='Clevel')

# 设置图表参数
plt.ylabel('Time (ns)')
plt.xlabel('Data Size')
plt.xticks([i + 2*width for i in x], labels)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=1.4)


# 保存图表为pdf
# plt.savefig(f'{file_name}.pdf', format='pdf')

# 显示图表
plt.show()