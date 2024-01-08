import numpy as np

data = []

filename = "zip.txt"
# filename = "uniform.txt"
with open(filename, "r") as file:
    for line in file:
        line = line.strip()  # 去除行尾的换行符和空格
        data.append(float(line))  # 将数据转换为浮点数并添加到列表中


# 计算P10、P50、P90
p10 = np.percentile(data, 10)
p50 = np.percentile(data, 50)
p90 = np.percentile(data, 90)
p99 = np.percentile(data, 99)
std_deviation = np.std(data)

# 计算方差
variance = np.var(data)

# 打印结果
print("P10:", p10)
print("P50:", p50)
print("P90:", p90)
print("P99:", p99)
print("Variance:", variance)
print("std_deviation:", std_deviation)