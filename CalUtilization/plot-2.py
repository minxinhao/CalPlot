import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 22
mpl.rcParams['pdf.fonttype'] = 42

# read data from CSV files
entry_data_df = pd.read_csv('entry_utilization.csv')
space_data_df = pd.read_csv('space_utilization.csv')

# define x-axis values
x = range(10, 267, 1)

# create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8))

# create plots in each subplot with adjusted linestyle and color
# ax1.plot(x, entry_data_df['SepHash'], label='SepHash', linestyle='-', color='black')
# ax1.plot(x, entry_data_df['RACE'], label='RACE', linestyle='--', color='gray')
# ax1.plot(x, entry_data_df['CLevel'], label='CLevel', linestyle='-.', color='black')
# ax1.plot(x, entry_data_df['Plush'], label='Plush', linestyle=':', color='gray')

# ax2.plot(x, space_data_df['SepHash'], label='SepHash', linestyle='-', color='black')
# ax2.plot(x, space_data_df['RACE'], label='RACE', linestyle='--', color='gray')
# ax2.plot(x, space_data_df['CLevel'], label='CLevel', linestyle='-.', color='black')
# ax2.plot(x, space_data_df['Plush'], label='Plush', linestyle=':', color='gray')

ax1.plot(x, entry_data_df['SepHash'], label='SepHash', linestyle='-')
ax1.plot(x, entry_data_df['RACE'], label='RACE', linestyle='--')
ax1.plot(x, entry_data_df['CLevel'], label='CLevel', linestyle='-.')
ax1.plot(x, entry_data_df['Plush'], label='Plush', linestyle=':')

ax2.plot(x, space_data_df['SepHash'], label='SepHash', linestyle='-')
ax2.plot(x, space_data_df['RACE'], label='RACE', linestyle='--')
ax2.plot(x, space_data_df['CLevel'], label='CLevel', linestyle='-.')
ax2.plot(x, space_data_df['Plush'], label='Plush', linestyle=':')

# add axis labels
ax1.set_xlabel("Number of Inserted KVs (thousands)")
ax2.set_xlabel("Number of Inserted KVs (thousands)")

# add legend
ax1.legend(loc='upper center', bbox_to_anchor=(1, 1.15), ncol=4, fontsize=22, framealpha=0, handlelength=2)

# add subplot titles below the figures
ax1.text(0.5, -0.2, '(a) Entry Utilization', transform=ax1.transAxes, fontsize=22, va='top', ha='center')
ax2.text(0.5, -0.2, '(b) Space Utilization', transform=ax2.transAxes, fontsize=22, va='top', ha='center')

# # set spines and tick colors
# for ax in [ax1, ax2]:
#     ax.spines['top'].set_color('gray')
#     ax.spines['bottom'].set_color('gray')
#     ax.spines['left'].set_color('gray')
#     ax.spines['right'].set_color('gray')
#     ax.xaxis.label.set_color('gray')
#     ax.yaxis.label.set_color('gray')
#     ax.tick_params(axis='x', colors='gray')
#     ax.tick_params(axis='y', colors='gray')

# adjust spacing between subplots and legend
plt.subplots_adjust(wspace=0.15, top=.93, bottom=.2, left=.046, right=1)

# save plot as a high-quality PDF file
plt.savefig('entry_space_utilization.pdf', dpi=300, bbox_inches='tight')

# show plot
plt.show()