import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

filename = 'insert_op_breakdown.csv' 

# read data from CSV file
data_df = pd.read_csv(filename)

# define x-axis values
x = range(1, 9, 1)
plt.figure(figsize=(10, 5.8))

# create plot
plt.plot(x, data_df['RACE']/1000, label='RACE', marker='o')
plt.plot(x, data_df['batch']/1000, label='batch', marker='s')
plt.plot(x, data_df['inline-dep']/1000, label='inline-dep', marker='x')
plt.plot(x, data_df['zero-wait write']/1000, label='zero-wait write', marker='^')

plt.xticks(x, ['1','2','4','8','16','32','64','128'])

# add title and axis labels
plt.xlabel('number of clients')
plt.ylabel("Throughput (Mops/s)")

# add legend
# plt.legend()
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=14, framealpha=0.8, handlelength=1)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=0.8)


# save plot as a high-quality PDF file
output_filename = '{}.pdf'.format(filename.split('.')[0])
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

# show plot
plt.show()