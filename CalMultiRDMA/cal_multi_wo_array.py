import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 读取Excel文件
# excel_file = 'insert.xlsx'
excel_file = 'search-wo-array.xlsx'
data = pd.read_excel(excel_file, header=None)

# 获取服务器数量
server_numbers = data.iloc[0, 1:].values.astype(float)

# 获取索引类型
index_types = data.iloc[1::4, 0].values
print(index_types)

# 初始化一个字典，用于存储每个索引类型的最大值
max_values = {}

# 遍历每个索引类型
print(data)
for i in range(1, data.shape[0], 4):
    index_type = data.iloc[i, 0]
    index_data = data.iloc[i:i+4, 1:5].values.astype(float)/1000
    index_data = index_data.T
    print(index_data)
    max_values[index_type] = [max(row) for row in index_data]

# 绘制折线图
print(server_numbers)
plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.1, top=.9,bottom=.11,left=0.14,right=.99)
markers = ['o', 's', 'x', '^', 'v', 'D','*', '>'] # 设置每个数据系列的标记样式

i = 0
for index_type, values in max_values.items():
    print(index_type)
    for val in reversed(values):
      print(val)
    plt.plot(server_numbers, values, label=index_type,marker=markers[i])
    i += 1
    # 在每个数据点上添加数值标签
    # for x, y in zip(server_numbers, values):
    #     plt.text(x, y, f'{y:.2f}', ha='center', va='bottom')

# 添加标题和标签
title = os.path.splitext(excel_file)[0]
# plt.title(title)
plt.xlabel('Server Number')
# plt.ylabel('Max Value')
plt.ylabel('Throughput (Mops)')

# 添加图例
# plt.legend()
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=18, framealpha=0, handlelength=0.8)


# 从Excel文件名提取不带扩展名的文件名
output_file = os.path.splitext(excel_file)[0] + '.pdf'

# 保存为高精度PDF文件
plt.savefig(output_file, dpi=300)

# 显示图形
plt.show()
