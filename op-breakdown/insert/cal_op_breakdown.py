import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 24
mpl.rcParams['pdf.fonttype'] = 42

filename = 'insert_op_breakdown.csv' 

# read data from CSV file
data_df = pd.read_csv(filename)

# define x-axis values
x = range(1, 9, 1)
plt.figure(figsize=(7, 6))
plt.subplots_adjust(wspace=0.1, top=1,bottom=.13,left=.13,right=.99)

# create plot
plt.plot(x, data_df['RACE']/1000, label='RACE', marker='o',markersize=10)
plt.plot(x, data_df['batch']/1000, label='Base', marker='s',markersize=10)
plt.plot(x, data_df['inline-dep']/1000, label='+resize-op entry', marker='x',markersize=10)
plt.plot(x, data_df['zero-wait']/1000, label='+zero-wait write', marker='^',markersize=10)

plt.xticks(x, ['1','2','4','8','16','32','64','128'])

# add title and axis labels
plt.xlabel('Number of clients',fontsize=24)
plt.ylabel("Throughput (Mops)")

# add legend
plt.legend(fontsize=24)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=14, framealpha=0.8, handlelength=1)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=.4)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=.4)

# add text below the plot
# plt.text(0.5, -0.18, '(a) insert optimization breakdown', horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=20)

# save plot as a high-quality PDF file
output_filename = '{}.pdf'.format(filename.split('.')[0])
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

# show plot
plt.show()