import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 22
mpl.rcParams['pdf.fonttype'] = 42

# 定义输入文件的名称
filename = 'max-rdma-throughputs.csv'

# 读取 CSV 文件并转换为 pandas DataFrame
df = pd.read_csv(filename, header=None, index_col=0)

# 获取每一行的最大值
max_values = df.max(axis=1)

# 将每个数据和对应的最大值相乘，然后将结果作为新的一列添加到 DataFrame 中
new_column_name = 'Throughput'
df[new_column_name] = df.index * max_values
df[new_column_name] = df[new_column_name].div(1024*1024)

# 获取每一行的最大值
max_values = max_values.div(1024)
access_latency = 1 / max_values
access_latency = access_latency * 100

# 创建一个水平柱状图
fig, ax = plt.subplots(figsize=(10, 5.8))
plt.subplots_adjust(wspace=0.1, top=.92,left=.1,right=.9,bottom=.125)
ax.bar(range(len(df.index)), access_latency, color='C0', label='access latency')

# 设置图形标题和坐标轴标签
# ax.set_title('Maximum Values')
ax.set_xlabel('access size(bytes)')
ax.set_ylabel('Latency(us)')

# 将数据名称作为 Y 轴标签
ax.set_xticks(range(len(max_values)))
ax.set_xticklabels(df.index)

# 添加新的一列数据的图形表示
ax2 = ax.twinx()
ax2.plot(range(len(df.index)), df[new_column_name], color='C1', marker='o', linewidth=5, label='Bandwidth')
ax2.set_ylabel('Bandwidth(GB/s)')
ax2.set_ylim(0, df[new_column_name].max() * 1.1)

# 添加图例
ax.legend(loc='upper left',bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=22, framealpha=0, handlelength=0.8)
ax2.legend(loc='upper right',bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=22, framealpha=0, handlelength=0.8)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=0.8)

# 显示图形
plt.savefig(f'RDMA-Thourghput-Latency.pdf', format='pdf')
plt.show()