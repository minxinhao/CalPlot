import numpy as np
import matplotlib.pyplot as plt

# 数据
categories = ['Insert', 'Search', 'Insert-Search (90:10)']
sep_hash_data = [10301.29, 88537.2, 14505.65]
dLSM_20MB_data = [1874.067, 1452.278, 1136.433]
dLSM_100MB_data = [6828.713, 1469.667, 6826.058]
dLSM_1GB_data = [39151.867, 1170.386, 6984.148]

# 设置柱状图宽度
bar_width = 0.15

# 设置位置
bar_positions1 = np.arange(len(categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width
bar_positions4 = bar_positions3 + bar_width

# 绘制柱状图
plt.bar(bar_positions1, sep_hash_data, width=bar_width, label='SepHash')
plt.bar(bar_positions2, dLSM_20MB_data, width=bar_width, label='dLSM-20MB')
plt.bar(bar_positions3, dLSM_100MB_data, width=bar_width, label='dLSM-100MB')
plt.bar(bar_positions4, dLSM_1GB_data, width=bar_width, label='dLSM-1GB')

# 设置刻度标签
plt.xticks(bar_positions2, categories)

# 添加标签和标题
plt.xlabel('Operation')
plt.ylabel('Time')
plt.title('Insert, Search, Insert-Search Performance')

# 添加图例
plt.legend()

# 展示图表
plt.show()