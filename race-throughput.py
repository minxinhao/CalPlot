import matplotlib.pyplot as plt

x = [1, 2, 4, 8, 16]
race_y = [40.37,82.85,158.59,235.78,342.83]
race_batch_y = [47.32, 96.54, 185.45, 339.28, 477.19]
no_split_y = [90.43, 181.76, 360.54, 643.12, 1085.98]

plt.plot(x, race_y, label="RACE/W Split")
plt.plot(x, no_split_y, label="RACE/Wo Split")
plt.plot(x, race_batch_y, label="RACE/Batch Move")
plt.xlabel("threads")
plt.ylabel("throughput (k ops/s)")
# plt.title("Insert Performance Comparison")
plt.legend()
plt.show()

