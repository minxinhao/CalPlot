import matplotlib.pyplot as plt

x = [1, 2, 4, 8, 16]
race_y = [40.37,82.85,158.59,235.78,342.83]
race_batch_y = [47.32, 96.54, 185.45, 339.28, 477.19]
no_split_y = [90.43, 181.76, 360.54, 643.12, 1085.98]

plt.figure(figsize=(6.4, 2.56))
plt.subplots_adjust(wspace=0.1, top=.1,left=.1,right=.99, bottom=.05)
plt.subplots_adjust(top=1,bottom=.17)
plt.plot(x, race_y, label="RACE/W Resize")
plt.plot(x, no_split_y, label="RACE/Wo Resize")
plt.plot(x, race_batch_y, label="RACE/Batch Move")
plt.xlabel("number of threads")
plt.ylabel("Throughput (Kops)")
# plt.title("Insert Performance Comparison")
plt.legend()
plt.savefig(f'race-throughput.pdf', format='pdf')
plt.show()

