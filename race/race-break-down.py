import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20
plt.rcParams['pdf.fonttype'] = 42

# 数据和标签
data = [0.16, 0.1, 0.13, 0.03, 0.14, 0.34, 0.10]
# labels = ['ReadBuc', 'CasEntry', 'ReRead','ReadSeg', 'ReadKv', 'MoveEntry', 'Other']
labels = ['Read\nBuc', 'Cas\nEntry', 'Re\nRead','Read\nSeg', 'Read\nKv', 'Move\nEntry', 'Other']

# 绘制直方图
# plt.figure(figsize=(6.4, 3))
plt.figure(figsize=(10, 5))
plt.subplots_adjust(wspace=0.1, top=.99,bottom=.14,left=.1,right=.99)
# plt.subplots_adjust(top=.99,bottom=.1)
rects = plt.bar(labels, data)

# 添加标签和标题
# plt.xlabel('Latency Breakdown')
plt.ylabel('Proportion')
plt.ylim(0,max(data)*1.1)
# plt.title('Insert Latency Breakdown in RACE')
# plt.xticks(rotation=-45)

# 在每个矩形上方显示相应的数值
for rect in rects:
    height = rect.get_height()
    plt.annotate(f'{height:.2f}',
                 xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 0),
                 textcoords='offset points',
                 ha='center', va='bottom')

# 显示图形
plt.savefig(f'race-break-down.pdf', format='pdf')
plt.show()
