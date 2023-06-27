import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

filename = 'entry_utilization.csv' 
# filename = 'space_utilization.csv'

# read data from CSV file
data_df = pd.read_csv(filename)

# define x-axis values
plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.1, top=.9,left=.12,right=.99)
# x = range(10000, 267000, 1000)
x = range(10, 267, 1)

# create plot
plt.plot(x, data_df['RACE'], label='RACE')
plt.plot(x, data_df['SepHash'], label='SepHash')
plt.plot(x, data_df['Clevel'], label='Clevel')
plt.plot(x, data_df['Plush'], label='Plush')

# add title and axis labels
plt.xlabel("Number of Inserted KVs(thousands)")
plt.ylabel(filename.split('.')[0])

# add legend
# plt.legend(loc='upper left',fontsize=20, framealpha=0, handlelength=.4)
# plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=14, framealpha=0.8, handlelength=1)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=18, framealpha=0, handlelength=.4)

# save plot as a high-quality PDF file
output_filename = '{}.pdf'.format(filename.split('.')[0])
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

# show plot
plt.show()
