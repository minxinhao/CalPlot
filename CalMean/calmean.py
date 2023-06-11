import csv
import statistics

# 打开 CSV 文件
with open('fp-num.csv', newline='') as csvfile:
    # 创建 CSV 读取器
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # 读取 CSV 文件中的每一行数据
    data = []
    for row in reader:
        # 转换每个字符串值为浮点数
        data.append(float(row[0]))

    # 计算数据的均值和标准差
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)

    # 计算数据的偏移程度
    skewness = statistics.mean([(x - mean) ** 3 for x in data]) / stdev ** 3

    # 打印计算结果
    print("The mean of the data is:", mean)
    print("The standard deviation of the data is:", stdev)
    print("The skewness of the data is:", skewness)