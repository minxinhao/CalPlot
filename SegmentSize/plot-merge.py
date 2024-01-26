import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 22
mpl.rcParams['pdf.fonttype'] = 42
# 输入数据
data1 = {
    '128B': (15728.04, 36567.54),
    '256B': (20684.51, 49672.22),
    '512B': (14323.71, 59123.59),
    '1KB': (9174.48, 73681.18),
    '2KB': (8869.82, 81233.05)    
}

data2 = {
    '8KB': (11834.04, 50317.33),
    '16KB': (10167.81, 61069.76),
    '32KB': (9174.48, 73681.18),
    '64KB': (10356.72, 84944.79)
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
bar_width = 0.4

# 创建图形和子图
fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(12, 5), sharey=False)

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


ax1.text(0.5, -0.12, '(a) Impact of CurSegment Size', transform=ax1.transAxes, fontsize=22, va='top', ha='center')
ax3.text(2, -0.12, '(b) Impact of MainSegment Size', transform=ax2.transAxes, fontsize=22, va='top', ha='center')

# 添加图例
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
# fig.legend(lines + lines2, labels + labels2, loc='upper center', ncol=2,framealpha=0, handlelength=.4)
fig.legend(lines + lines2, labels + labels2, loc='upper center', ncol=2, fontsize=22,framealpha=0, handlelength=.4, bbox_to_anchor=(.5, 1.05))
# ax1.legend(labels+labels2,loc='upper center',bbox_to_anchor=(1, 1.15), ncol=2, fontsize=22, framealpha=0, handlelength=2)

plt.subplots_adjust(wspace=0.5, top=.93,bottom=.15,left=.08,right=.93)

# 设置图形标题
# plt.suptitle('Insert and Search Performance')

# 调整图形布局
# plt.tight_layout()
plt.savefig(f'Segment-Size.pdf', format='pdf', dpi=300)

# 展示图形
plt.show()