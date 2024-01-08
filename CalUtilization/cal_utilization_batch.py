
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# read data from CSV files
entry_data_df = pd.read_csv('entry_utilization.csv')
space_data_df = pd.read_csv('space_utilization.csv')

# define x-axis values
x = range(10, 267, 1)

# create subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8), sharey=True)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8))

# create plots in each subplot
ax1.plot(x, entry_data_df['SepHash'], label='SepHash')
ax1.plot(x, entry_data_df['RACE'], label='RACE')
ax1.plot(x, entry_data_df['CLevel'], label='CLevel')
ax1.plot(x, entry_data_df['Plush'], label='Plush')

ax2.plot(x, space_data_df['SepHash'], label='SepHash')
ax2.plot(x, space_data_df['RACE'], label='RACE')
ax2.plot(x, space_data_df['CLevel'], label='CLevel')
ax2.plot(x, space_data_df['Plush'], label='Plush')

# add axis labels
ax1.set_xlabel("Number of Inserted KVs (thousands)")
# ax1.set_ylabel("Entry Utilization")
ax2.set_xlabel("Number of Inserted KVs (thousands)")
# ax2.set_ylabel("Space Utilization")

# add legend
ax1.legend(loc='upper center',bbox_to_anchor=(1, 1.2), ncol=4, fontsize=20, framealpha=0, handlelength=2)

# add subplot titles below the figures
ax1.text(0.5, -0.2, '(a) Entry Utilization', transform=ax1.transAxes, fontsize=20, va='top', ha='center')
ax2.text(0.5, -0.2, '(b) Space Utilization', transform=ax2.transAxes, fontsize=20, va='top', ha='center')

# adjust spacing between subplots and legend
plt.subplots_adjust(wspace=0.15, top=.88,bottom=.2,left=.046,right=1)

# save plot as a high-quality PDF file
plt.savefig('entry_space_utilization.pdf', dpi=300, bbox_inches='tight')

# show plot
plt.show()