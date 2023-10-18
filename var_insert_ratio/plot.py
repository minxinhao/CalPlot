import matplotlib.pyplot as plt
import numpy as np

data = {
    "10% : 90%": {
        "race": [38745.28, 38392.86, 38126.79, 43430.29],
        "sephash": [33324.55, 23393.16, 34219.85, 32528.72],
        "clevel": [5636.42, 5394.79, 8376.28, 13154.03],
        "plush": [5179.04, 4454.97, 5667.68, 8758.2]
    },
    "30% : 70%": {
        "race": [28256.879999999997, 30293.43, 25652.67, 21373.07],
        "sephash": [24741.47, 14790.61, 23668.89, 21464.19],
        "clevel": [7011.33, 6740.07, 6015.09, 6835.85],
        "plush": [5276.08, 4836.88, 4872.92, 3616.72]
    },
    "50% : 50%": {
        "race": [2263.71, 1770.82, 1468.3, 928.4],
        "sephash": [14925.88, 17194.45, 18453.72, 13123.39],
        "clevel": [6330.85, 6943.72, 7544.2, 7936.3],
        "plush": [5024.1, 4906.8, 4316, 3858]
    },
    "70% : 30%": {
        "race": [2198.6, 1007.56, 645.77, 366.55],
        "sephash": [16315.32, 11457.41, 16415.57, 12931.95],
        "clevel": [5540.13, 5540.63, 5859.08, 6729.94],
        "plush": [4966.56, 3236.74, 2755.7, 2419.1]
    },
    "90% : 10%": {
        "race": [2181.15, 643.25, 539.56, 431.49],
        "sephash": [16154.81, 14006.63, 11138.43, 15787.39],
        "clevel": [5001.69, 4655.24, 6300.84, 8621.76],
        "plush": [5738.42, 2930.96, 2720.24, 2322.62]
    }
}

# 提取索引和对应的数据
indexes = list(data[next(iter(data))].keys())  # 获取索引名称列表
ratios = list(data.keys())  # 获取比例列表
values = np.zeros((len(ratios), len(indexes)))  # 创建值的矩阵

for i, ratio in enumerate(ratios):
    for j, index in enumerate(indexes):
        values[i, j] = max(data[ratio][index])

# 绘制柱状图
x = np.arange(len(ratios))
width = 0.15
fig, ax = plt.subplots(figsize=(10, 6))
rects = []

for i, index in enumerate(indexes):
    rects.append(ax.bar(x + i * width, values[:, i], width, label=index))

# 添加标签
ax.set_ylabel('Max Value')
ax.set_xlabel('Insert-Search Ratios')
ax.set_title('Max Values for Each Index')
ax.set_xticks(x + width * (len(indexes) - 1) / 2)  # 调整刻度的位置
ax.set_xticklabels(ratios)
ax.legend()

# 保存为高精度的PDF文件
plt.tight_layout()
# plt.savefig('chart.pdf', dpi=300, format='pdf')

plt.show()