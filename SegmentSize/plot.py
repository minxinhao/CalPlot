import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20
# 输入数据
data = {
    '2KB': (8869.82, 81233.05),
    '1KB': (9174.48, 73681.18),
    '512B': (14323.71, 59123.59),
    '256B': (20684.51, 49672.22),
    '128B': (15728.04, 36567.54)
}

# 分离数据
segments = list(data.keys())
insert_data = [data[key][0]/1000 for key in segments]
search_data = [data[key][1]/1000 for key in segments]
x_ticks = np.arange(len(segments))

# 设置柱状图的宽度
bar_width = 0.35

# 创建图形
fig, ax = plt.subplots(figsize=(7, 5.8))

# 绘制Insert柱状图
ax.bar(x_ticks, insert_data, bar_width, color='tab:blue', label='Insert')

# 设置x轴刻度和标签
ax.set_xticks(x_ticks)
ax.set_xticklabels(segments)

# 创建副坐标轴
ax2 = ax.twinx()

# 绘制Search柱状图
ax2.bar(x_ticks + bar_width, search_data, bar_width, color='tab:orange', label='Search')

# 设置y轴标签
ax.set_ylabel('Insert TP(MIops)')
ax2.set_ylabel('Search TP(MIops)')

# 添加图例
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
# ax.legend(lines + lines2, labels + labels2, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=2,fontsize=20, framealpha=0, handlelength=2)
# ax.text(0.5, -0.2, '(a) Impact of CurSegment Size', transform=ax.transAxes, fontsize=20, va='top', ha='center')
plt.subplots_adjust(wspace=0.3, top=1,bottom=.06,left=.15,right=.88)

# 设置图形标题
# plt.title('Insert and Search Performance')

# 调整图形布局
# plt.tight_layout()
plt.savefig(f'CurSegment-Size.pdf', format='pdf', dpi=300)

# 展示图形
plt.show()
