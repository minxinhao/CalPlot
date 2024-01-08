import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 16
# 数据
# labels = ['8 bytes', '16 bytes', '32 bytes', '64 bytes', '128 bytes', '256 bytes', '512 bytes', '1 KB', '2 KB', '4 KB']
labels = ['8 bytes', '16 bytes', '32 bytes', '64 bytes', '128 bytes', '256 bytes', '512 bytes', '1024 bytes', '2048 bytes', '4096 bytes']
key_values = [9489.86, 9453.79, 9468.62, 9470.56, 9544.43, 9565.28, 9588.79, 9425.21, 9033.88, 8396.72]
key_values = np.array(key_values)/1000
value_values = [9695.32, 9651.35, 9808.21, 9836.59, 9699.77, 9688.42, 9701.66, 9510.38, 8975.43, 8636.55]
value_values = np.array(value_values)/1000
key_values_2 = [76142.36, 75019.71, 75746.77, 74237.44, 73152.21, 72694.1, 61821.25, 42706.73, 29476.98, 18141.8]
key_values_2 = np.array(key_values_2)/1000
value_values_2 = [76741.07, 75127.15, 74652.29, 74484.56, 74029.66, 74607.89, 58293.79, 38951.27, 30707.63, 18314.04]
value_values_2 = np.array(value_values_2)/1000

x = np.arange(len(labels))  # x轴位置
width = 0.35  # 柱状图宽度

# 创建图形对象和两个子图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5.8))
plt.subplots_adjust(wspace=0.2, top=.9,bottom=.25,left=0.08,right=.99)

# 绘制第一个子图
rects1 = ax1.bar(x - width/2, key_values, width, label='Key-Size')
rects2 = ax1.bar(x + width/2, value_values, width, label='Value-Size')
ax1.set_xlabel('(a)Insert performance')
ax1.set_ylabel('Throughput (Mops)')
# ax1.set_title('Data Access Time - Dataset 1')
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45)
# ax1.set_xticklabels(labels, rotation=45, ha='right')  # 设置刻度标签向左对齐
# ax1.set_xticklabels(labels)
# ax1.legend()
ax1.legend(loc='upper center', bbox_to_anchor=(1.1, 1.15), ncol=4, fontsize=16,framealpha=0, handlelength=.4)


# 添加数值标签
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax1.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)

# 绘制第二个子图
rects3 = ax2.bar(x - width/2, key_values_2, width, label='Key')
rects4 = ax2.bar(x + width/2, value_values_2, width, label='Value')
ax2.set_xlabel('(b)Search performance')
ax2.set_ylabel('Throughput (Mops)')
# ax2.set_title('Data Access Time - Dataset 2')
ax2.set_xticks(x)
ax2.set_xticklabels(labels, rotation=45)
# ax2.set_xticklabels(labels, rotation=45, ha='right')  # 设置刻度标签向左对齐
# ax2.legend()

# autolabel(rects3)
# autolabel(rects4)
plt.savefig("var_kv.pdf", dpi=300)

# 调整布局并显示图形
# plt.tight_layout()
plt.show()