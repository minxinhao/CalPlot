import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['legend.fontsize'] = 10
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.legend(loc='upper left', fontsize=10)

# 定义输入文件的名称
# filename = 'micro_bench_insert.csv' 
# filename = 'MainSegSize-Search.csv' 
filename = 'YCSB-D.csv' 
# filename = 'CurSegSize-Search.csv' 

# 从CSV文件读取数据
with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        name = row[0]
        values = [float(x) for x in row[1:-1]]
        data.append([name] + values)

# 使用原始数据中的代码绘制折线图
groups = []
for row in data:
    name = row[0]
    values = row[1:]
    group = []
    for i in range(0, len(values), 4):
        group.append(max(values[i:i+4]))
    groups.append((name, group))

x_labels = ['1', '2', '4', '8', '16', '32', '64', '128'] # 将标签存储为字符串

# plt.figure(figsize=(10, 6), dpi=300)
markers = ['o', 's', 'x', '^', 'v', 'D','*', '>'] # 设置每个数据系列的标记样式

# 定义输出文件的名称，使用字符串格式化
output_filename = '{}.pdf'.format(filename.split('.')[0])

for i, (name, group) in enumerate(groups):
    y_data = np.array(group) / 1000 # 将数据除以10
    plt.plot(x_labels, y_data, label=name, marker=markers[i]) # 指定标记样式
plt.xlabel("Number of Threads")
plt.ylabel("Throughput (Mops/s)")
# plt.legend()
plt.legend(loc='upper left', fontsize=10)

# 将输出文件保存到指定名称
# plt.savefig(output_filename)

# # 显示图片
plt.show()