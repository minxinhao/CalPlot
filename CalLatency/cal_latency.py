import argparse
import statistics

def calculate_median(values):
    return statistics.median(values)

def calculate_average(values):
    return statistics.mean(values)

def calculate_p99(values):
    return statistics.quantiles(values, n=100)[98]

def calculate_p999(values):
    return statistics.quantiles(values, n=1000)[998]

# 创建命令行参数解析器
parser = argparse.ArgumentParser(description='计算操作延迟统计信息')
parser.add_argument('operation', choices=['insert', 'search'], help='操作参数：insert 或 search')
parser.add_argument('server_count', type=int, help='服务器数量')


# 解析命令行参数
args = parser.parse_args()

operation = args.operation
server_count = args.server_count

latencies = []
server_ip = ['192.168.1.52', '192.168.1.53', '192.168.1.51', '192.168.1.33', '192.168.1.44', '192.168.1.69', '192.168.1.88', '192.168.1.89']
filename_prefix = f"{operation}_lat"
cli_num = 16
coro_num = 4
all_filenames = []  # 新增空列表用于存储所有的 filenames
for cli_num in range(cli_num + 1):
    for coro_num in range(coro_num + 1):
        filenames = [f"{filename_prefix}{cli_num}{coro_num}{server_ip[i]}.txt" for i in range(server_count)]
        all_filenames.extend(filenames)  # 将生成的 filenames 追加到 all_filenames
print(len(all_filenames))
print(all_filenames)
# 选择要处理的文件数量

# 读取文件并提取时延数据
for filename in all_filenames:
    try:
        with open(filename, "r") as file:
            for line in file:
                latency = float(line.strip())
                latencies.append(latency)
    except FileNotFoundError:
        print(f"无法打开文件: {filename}")

print(len(latencies))
# 计算中位数、平均值和 P99 值
median = calculate_median(latencies)
average = calculate_average(latencies)
p99 = calculate_p99(latencies)
p999 = calculate_p999(latencies)

# 输出结果
print("中位数延迟:", median)
print("平均延迟:", average)
print("P99 延迟:", p99)
print("P999 延迟:", p999)