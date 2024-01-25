import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20
mpl.rcParams['pdf.fonttype'] = 42

# 数据
sep_hash = np.array([56161.16, 74343.55, 88537.2, 68007.14]) / 1000
race = np.array([69204.72, 81000, 99710.3, 83460.82]) / 1000
clevel = np.array([7417.05, 8748.4, 11120.05, 9543.89]) / 1000
plush = np.array([5200.35, 4270.93, 3893.1, 4348.51]) / 1000
x_labels = ['YCSB-A', 'YCSB-B', 'YCSB-C', 'YCSB-D']
legend_labels = ['SepHash', 'RACE', 'CLevel', 'Plush']

# # 绘图
# plt.figure(figsize=(10, 5.8))
# x = np.arange(len(x_labels))  # x 轴坐标
# width = 0.2  # 柱宽
# plt.bar(x - 1.5 * width, sep_hash, width, label=legend_labels[0])
# plt.bar(x - 0.5 * width, race, width, label=legend_labels[1])
# plt.bar(x + 0.5 * width, plush, width, label=legend_labels[2])
# plt.bar(x + 1.5 * width, clevel, width, label=legend_labels[3])
# plt.xticks(x, x_labels)
# plt.ylabel('Throughput (Mops/s)')

# # 设置图例
# # plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4, fontsize=14)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=1.4)

# 绘图
plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.001, top=.9,bottom=.06,left=.14,right=.99)
x = np.arange(len(x_labels))  # x 轴坐标
width = 0.2  # 柱宽
plt.bar(x - 1.5 * width, sep_hash, width, label=legend_labels[0], edgecolor='black')
plt.bar(x - 0.5 * width, race, width, label=legend_labels[1], edgecolor='black')
plt.bar(x + 0.5 * width, plush, width, label=legend_labels[2], edgecolor='black')
plt.bar(x + 1.5 * width, clevel, width, label=legend_labels[3], edgecolor='black')
plt.xticks(x, x_labels)
plt.ylabel('Throughput (Mops)')

# 设置图例
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=4, fontsize=14)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=18, framealpha=0, handlelength=.4)

plt.savefig("ycsb_performance.pdf")

# 显示图形
plt.show()
