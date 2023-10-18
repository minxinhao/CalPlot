import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 数据
MainSeg_CurSeg = [64, 32, 16, 8]
Naive = [9, 18, 32, 64]
Record_Point = [2.88, 5.36, 10.72, 20]


plt.figure(figsize=(7, 5))
plt.subplots_adjust(wspace=0.001, top=.99,bottom=.06,left=.14,right=.99)

# 设置柱状图的宽度
bar_width = 0.35

# 计算柱状图的位置
bar_positions1 = np.arange(len(MainSeg_CurSeg))
bar_positions2 = bar_positions1 + bar_width

# 创建柱状图
plt.bar(bar_positions1, Naive, width=bar_width, label='Naive')
plt.bar(bar_positions2, Record_Point, width=bar_width, label='Record Point')

# 添加标签和标题
plt.xlabel('MainSeg/CurSeg')
plt.ylabel('Size (MB)')
# plt.title('Comparison of Naive and Record Point')
plt.xticks(bar_positions1 + bar_width/2, MainSeg_CurSeg)

# 添加图例
plt.legend()

plt.savefig("cache-space.pdf", format='pdf', dpi=300)

# 显示图形
plt.show()