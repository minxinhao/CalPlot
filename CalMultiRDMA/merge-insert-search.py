import pandas as pd
import matplotlib.pyplot as plt
import os
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 读取Excel文件
insert_excel_file = 'insert.xlsx'
search_excel_file = 'search.xlsx'

# 创建一个包含两个子图的图形
fig, axes = plt.subplots(1, 2, figsize=(14, 5.8))
fig.subplots_adjust(wspace=0.3, top=0.88, bottom=0.2,left=0.08, right=.99)

# 处理插入数据的Excel文件
insert_data = pd.read_excel(insert_excel_file, header=None)

# 获取服务器数量
insert_server_numbers = insert_data.iloc[0, 1:].values.astype(float)

# 获取索引类型
insert_index_types = insert_data.iloc[1::4, 0].values

# 初始化一个字典，用于存储每个索引类型的最大值
insert_max_values = {}
markers = ['o', 's', 'x', '^', 'v', 'D','*', '>'] # 设置每个数据系列的标记样式

# 遍历每个索引类型
for i in range(1, insert_data.shape[0], 4):
    index_type = insert_data.iloc[i, 0]
    index_data = insert_data.iloc[i:i+4, 1:5].values.astype(float)/1000
    index_data = index_data.T
    insert_max_values[index_type] = [max(row) for row in index_data]

# 绘制插入数据的折线图
i = 0 
for index_type, values in insert_max_values.items():
    axes[0].plot(insert_server_numbers, values, label=index_type,marker=markers[i])
    i += 1

# 添加标签
axes[0].set_xlabel('Server Number')
axes[0].set_ylabel('Throughputs(MIops)')

# 处理搜索数据的Excel文件
search_data = pd.read_excel(search_excel_file, header=None)

# 获取服务器数量
search_server_numbers = search_data.iloc[0, 1:].values.astype(float)

# 获取索引类型
search_index_types = search_data.iloc[1::4, 0].values

# 初始化一个字典，用于存储每个索引类型的最大值
search_max_values = {}

# 遍历每个索引类型
for i in range(1, search_data.shape[0], 4):
    index_type = search_data.iloc[i, 0]
    index_data = search_data.iloc[i:i+4, 1:5].values.astype(float)/ 1000
    index_data = index_data.T
    search_max_values[index_type] = [max(row) for row in index_data]

# 绘制搜索数据的折线图
i = 0 
for index_type, values in search_max_values.items():
    axes[1].plot(search_server_numbers, values, label=index_type,marker=markers[i])
    i += 1

# 添加标签
axes[1].set_xlabel('Server Number')
axes[1].set_ylabel('Throughputs(MIops)')

# 共享图例
handles, labels = axes[1].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1), ncol=len(labels),framealpha=0, handlelength=2)

axes[0].text(0.5, -0.2, '(a) insert performance', transform=axes[0].transAxes, fontsize=20, va='top', ha='center')
axes[1].text(0.5, -0.2, '(b) search performance', transform=axes[1].transAxes, fontsize=20, va='top', ha='center')


# 保存为高精度PDF文件
output_file = 'multi-server.pdf'
plt.savefig(output_file, dpi=300)

# 显示图形
plt.show()