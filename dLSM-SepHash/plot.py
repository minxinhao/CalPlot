import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 16
# 数据
# categories = ['Insert', 'Search', 'Insert-Search (1:9)','Insert-Search (5:5)','Insert-Search (9:1)']
# categories = ['Search', '10% Insert','50% Insert','90% Insert','Insert']
# categories = ['Search', '9:1','5:5','1:9','Insert']
# sep_hash_data = [88537.2, 33324.55, 14925.88, 14505.65,10301.29]
# dLSM_20MB_data = [1452.278, 1816.542, 1472.351, 1136.433,1874.067]
# dLSM_40MB_data = [1452.278, 1754.245, 2424.556, 1136.433,1874.067]
# dLSM_100MB_data = [1469.667, 1930.932, 3514.639, 6826.058,6828.713]
# dLSM_1GB_data = [ 1170.386, 2752.476, 4608.564, 6984.148,39151.867]

# categories = ['Only\nSearch', '7:3','5:5','3:7','Only\nInsert']
categories = ['Only-Search', '7:3','5:5','3:7','Only-Insert']
sep_hash_data = [88537.2, 33324.55, 14925.88, 14505.65,10301.29]
dLSM_20MB_data = [1452.278, 2013.596, 1472.351, 1333.875,1874.067]
dLSM_40MB_data = [1452.278, 2188.621, 2424.556, 3308.381,1874.067]
dLSM_100MB_data = [1469.667, 3092.562, 3514.639, 4541.488,6828.713]
dLSM_1GB_data = [ 1170.386, 3209.763, 4608.564, 6302.793,39151.867]

sep_hash_data = np.array(sep_hash_data) / 1000
dLSM_20MB_data = np.array(dLSM_20MB_data) / 1000
dLSM_40MB_data = np.array(dLSM_40MB_data) / 1000
dLSM_100MB_data = np.array(dLSM_100MB_data) / 1000
dLSM_1GB_data = np.array(dLSM_1GB_data) / 1000

# 设置柱状图宽度
bar_width = 0.15

# 设置位置
bar_positions1 = np.arange(len(categories))
bar_positions2 = bar_positions1 + bar_width
bar_positions3 = bar_positions2 + bar_width
bar_positions4 = bar_positions3 + bar_width
bar_positions5 = bar_positions4 + bar_width

plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.1, top=1,bottom=.11,left=0.1,right=.99)

# 绘制柱状图
plt.bar(bar_positions1, sep_hash_data, width=bar_width, label='SepHash')
plt.bar(bar_positions2, dLSM_20MB_data, width=bar_width, label='dLSM-20MB')
plt.bar(bar_positions3, dLSM_40MB_data, width=bar_width, label='dLSM-40MB')
plt.bar(bar_positions4, dLSM_100MB_data, width=bar_width, label='dLSM-100MB')
plt.bar(bar_positions5, dLSM_1GB_data, width=bar_width, label='dLSM-1GB')

# 设置刻度标签
plt.xticks(bar_positions2, categories)

# 添加标签和标题
plt.xlabel('Search/Insert operation ratio')
plt.ylabel('Throughput (Mops)')
# plt.title('Insert, Search, Insert-Search Performance')

# 添加图例
plt.legend()

plt.savefig(f'dLSM-SepHash.pdf', format='pdf', dpi=300)

# 展示图表
plt.show()