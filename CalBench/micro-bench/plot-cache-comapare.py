import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 定义输入文件的名称
# filename = 'micro_bench_insert.csv' 
filename = 'ycsb_search.csv' 
# filename = 'MainSegSize-Search.csv' 
# filename = 'YCSB-D.csv' 
# filename = 'CurSegSize-Insert.csv' 

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
output_filename = '{}-cache.pdf'.format(filename.split('.')[0])

plt.figure(figsize=(7.5, 5.8))
# plt.subplots_adjust(wspace=0.1, top=1,left=.1,right=.99)
plt.subplots_adjust(wspace=0.1, top=.88,bottom=.11,left=0.14,right=.95)

for i, (name, group) in enumerate(groups):
    y_data = np.array(group) / 1000 # 将数据除以10
    print(name, y_data)
    plt.plot(x_labels, y_data, label=name, marker=markers[i],markersize=8) # 指定标记样式
plt.xlabel("Number of Threads")
plt.ylabel("Throughput (Mops)")
plt.legend(fontsize=20) # 调
# 整图例字体大小
plt.legend(loc='upper center', bbox_to_anchor=(0.45, 1.2), ncol=3, fontsize=18, framealpha=0, handlelength=0.8)


# 将输出文件保存到指定名称
plt.savefig(output_filename)

# # 显示图片
plt.show()