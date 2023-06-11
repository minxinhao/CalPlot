import matplotlib.pyplot as plt

# 绘图
fig, ax = plt.subplots()

# 绘制两条横线
ax.hlines(y=0, xmin=0, xmax=18, colors='gray', linestyles='dashed', label='RTT')
ax.hlines(y=1, xmin=0, xmax=18, colors='gray', linestyles='dashed')

# 绘制六条折线
ax.plot([0, 3, 3, 6, 6, 9, 9, 12, 12, 15, 15, 18], [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], label='RTT')

# 添加标签及标题
ax.set_xlabel('Time (ms)')
ax.set_ylabel('RTT')
ax.set_title('Three-Way RTT')

# 图例
ax.legend()

# 显示图形
plt.show()