import matplotlib.pyplot as plt

# 数据和标签
data = [0.16, 0.1, 0.13, 0.03, 0.14, 0.34, 0.07]
labels = ['ReadBuc', 'CasSlot', 'ReRead','ReadSeg', 'ReadKv', 'MoveEntry', 'Other']

# 绘制直方图
rects = plt.bar(labels, data)

# 添加标签和标题
# plt.xlabel('Latency Breakdown')
plt.ylabel('Proportion')
# plt.title('Insert Latency Breakdown in RACE')

# 在每个矩形上方显示相应的数值
for rect in rects:
    height = rect.get_height()
    plt.annotate(f'{height:.2f}',
                 xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords='offset points',
                 ha='center', va='bottom')

# 显示图形
plt.show()