import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 16
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
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(12, 5.8), sharey=False)

# 绘制第一个子图的Insert柱状图
ax1.bar(x_ticks1, insert_data1, bar_width, color='tab:blue', label='Insert')
# 设置第一个子图的x轴刻度和标签
ax1.set_xticks(x_ticks1)
ax1.set_xticklabels(segments1)

# 创建副坐标轴
ax2 = ax1.twinx()

# 绘制Search柱状图
ax2.bar(x_ticks1 + bar_width, search_data1, bar_width, color='tab:orange', label='Search')

# 设置y轴标签
ax1.set_ylabel('Insert Throughput(Mops)')
ax2.set_ylabel('Search Throughput(Mops)')


# 绘制第二个子图的Insert柱状图
ax3.bar(x_ticks2, insert_data2, bar_width, color='tab:blue', label='Insert')
# 设置第二个子图的x轴刻度和标签
ax3.set_xticks(x_ticks2)
ax3.set_xticklabels(segments2)

# 创建副坐标轴
ax4 = ax3.twinx()

# 绘制Search柱状图
ax4.bar(x_ticks2 + bar_width, search_data2, bar_width, color='tab:orange', label='Search')
# 设置y轴标签
ax3.set_ylabel('Insert Throughput(Mops)')
ax4.set_ylabel('Search Throughput(Mops)')


ax1.text(0.5, -0.2, '(a) Impact of CurSegment Size', transform=ax1.transAxes, fontsize=20, va='top', ha='center')
ax3.text(1.8, -0.2, '(b) Impact of MainSegment Size', transform=ax2.transAxes, fontsize=20, va='top', ha='center')

# 添加图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines + lines2, labels + labels2, loc='upper center', ncol=2,framealpha=0, handlelength=.4)
# ax1.legend(labels+labels2,loc='upper center',bbox_to_anchor=(1, 1.15), ncol=2, fontsize=20, framealpha=0, handlelength=2)

plt.subplots_adjust(wspace=0.4, top=.9,bottom=.2,left=.08,right=.93)

# 设置图形标题
# plt.suptitle('Insert and Search Performance')

# 调整图形布局
# plt.tight_layout()
plt.savefig(f'Segment-Size.pdf', format='pdf', dpi=300)

# 展示图形
plt.show()