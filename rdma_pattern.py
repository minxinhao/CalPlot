import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('rdma-pattern.csv', header=None)

# 提取访问粒度和线程数-协程数
access_sizes = ["64B", "128B", "256B", "512B", "1KB", "2KB", "4KB"]
thread_coroutines = [f"{i}-{j}" for i in range(1, 65) for j in range(1, 9)]
# 将数据重塑为DataFrame
data = df.values.reshape((len(access_sizes) * len(thread_coroutines), -1))
df_new = pd.DataFrame(data=data, columns=["Ops"] * 8)

# 添加访问粒度和线程数-协程数列
df_new["Access Size"] = [f"{size}" for size in access_sizes for _ in range(len(thread_coroutines))]
df_new["Thread-Coroutine"] = thread_coroutines * len