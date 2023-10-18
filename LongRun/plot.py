import matplotlib.pyplot as plt
import numpy as np

# 原始数据
data = {
    'SepHash': {
        'split_cnt': 87496,
        'split_time': 2.53E+07,
        'insert_time': 3.76E+09,
        'split_ratio': 0.006726941,
        'LevelCnt': 1,
        'RetryCnt': 8.0494734
    },
    'RACE': {
        'split_cnt': 2568535,
        'split_time': 7.74E+10,
        'insert_time': 1.74967E+11,
        'split_ratio': 0.442415135,
        'LevelCnt': 1,
        'RetryCnt': 3.817233161
    },
    'Plush': {
        'split_cnt': 59549,
        'split_time': 1.93E+10,
        'insert_time': 5.01E+11,
        'split_ratio': 0.038513655,
        'LevelCnt': 3,
        'RetryCnt': 1
    },
    'CLevel': {
        'split_cnt': 18,
        'split_time': 870.634,
        'insert_time': 1.13E+10,
        'split_ratio': 0.015205042,
        'LevelCnt': 8,
        'RetryCnt': 8.277397851
    }
}

# 提取要绘制的数据项和数值
x_labels = list(data.keys())
split_cnt_values = [data[label]['split_cnt'] for label in x_labels]
split_time_values = [data[label]['split_time'] for label in x_labels]
insert_time_values = [data[label]['insert_time'] for label in x_labels]
split_ratio_values = [data[label]['split_ratio'] for label in x_labels]
level_cnt_values = [data[label]['LevelCnt'] for label in x_labels]
retry_cnt_values = [data[label]['RetryCnt'] for label in x_labels]

# 设置图形大小
plt.figure(figsize=(10, 6))

# 绘制堆叠柱状图
plt.bar(x_labels, split_cnt_values, label='Split Count')
plt.bar(x_labels, split_time_values, bottom=split_cnt_values, label='Split Time')
plt.bar(x_labels, insert_time_values, bottom=np.add(split_cnt_values, split_time_values), label='Insert Time')

# 添加标签和标题
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Comparison of Different Data')

# 添加图例
plt.legend()

# 调整x轴标签的角度，以避免重叠
plt.xticks(rotation=45)

# 展示图形
plt.show()