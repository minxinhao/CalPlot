import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 输入数据
data1 = {
    '2KB': (8869.82, 81233.05),
    '1KB': (9174.48, 73681.18),
    '512B': (14323.71, 59123.59),
    '256B': (20684.51, 49672.22),
    '128B': (15728.04, 36567.54)
}

data2 = {
    '64KB': (10356.72, 84944.79),
    '32KB': (9174.48, 73681.18),
    '16KB': (10167.81, 61069.76),
    '8KB': (11834.04, 50317.33)
}

# 分离数据
segments1 = list(data1.keys())
insert_data1 = [data1[key][0]/1000 for key in segments1]
search_data1 = [data1[key][1]/1000 for key in segments1]
x_ticks1 = np.arange(len(segments1))

segments2 = list(data2.keys())
insert_data2 = [data2[key][0]/1000 for key in segments2]
search_data2 = [data2[key][1]/1000 for key in segments2]
x_ticks2 = np.arange(len(segments2))

# 设置柱状图的宽度
bar_width = 0.35

# 创建图形和子图
fig, ax1 = plt.subplots(figsize=(12, 5.8))
ax2 = ax1.twinx()

# 绘制第一个子图的Insert柱状图
ax1.bar(x_ticks1, insert_data1, bar_width, color='tab:blue', label='Insert')

# 绘制第一个子图的Search柱状图
ax1.bar(x_ticks1 + bar_width, search_data1, bar_width, color='tab:orange', label='Search')

# 设置第一个子图的x轴刻度和标签
ax1.set_xticks(x_ticks1)
ax1.set_xticklabels(segments1)

# 设置第一个子图的y轴标签
ax1.set_ylabel('Insert Throughputs (MIops)')

# 设置第二个子图的y轴标签
ax2.set_ylabel('Search Throughputs (MIops)')

# 绘制第二个子图的Insert柱状图
ax2.bar(x_ticks2, insert_data2, bar_width, color='tab:blue', alpha=0.5, label='Insert')

# 绘制第二个子图的Search柱状图
ax2.bar(x_ticks2 + bar_width, search_data2, bar_width, color='tab:orange', alpha=0.5, label='Search')

# 设置第二个子图的x轴刻度和标签
ax2.set_xticks(x_ticks2)
ax2.set_xticklabels(segments2)

# 添加图例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=16, framealpha=0, handlelength=2)

# 添加子图标签
ax1.text(0.5, -0.2, '(a) Impact of CurSegment Size', transform=ax1.transAxes, fontsize=20, va='top', ha='center')
ax2.text(0.5, -0.2, '(b) Impact of MainSegment Size', transform=ax2.transAxes, fontsize=20, va='top', ha='center')

# 调整图形布局
plt.subplots_adjust(top=.88, bottom=.2, left=.08, right=1)

# 展示图形
plt.show()