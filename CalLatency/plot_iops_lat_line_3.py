import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# Read the data from the CSV file
filename = 'search-latency'
# filename = 'insert-latency'
# data = pd.read_csv('insert-latency.csv', delimiter=',', index_col=0, skip_blank_lines=True)
data = pd.read_csv(f'{filename}.csv', delimiter=',', index_col=0, skip_blank_lines=True)

# Get the x labels from the first row of delay_data
x_labels = list(data.columns)

throughputs = data.loc['throughputs'].astype(np.float64)/1000

correspond_p10_delay = data.loc['P10 latency'].astype(np.float64)
correspond_p999_delay = data.loc['P9999 latency'].astype(np.float64)
correspond_p999_delay = np.log10(correspond_p999_delay)

# Create a dictionary to map index labels to colors and markers
colors_markers = {'SepHash': {'color': 'b', 'marker': 'o'}, 
                  'RACE': {'color': 'y', 'marker': 's'}, 
                  'CLevel':   {'color': 'g', 'marker': 'x'},
                  'Plush': {'color': 'r', 'marker': '^'}
                  }

# Create a figure and axis for the plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.8))
fig.subplots_adjust(hspace=0.4, top=.88, bottom=0.2, left=0.08, right=.99)

# Iterate over each index label (RACE, SepHash, Plush, CLevel)
i = 0
for index_label, properties in colors_markers.items():
    # Create lists to store the selected data
    selected_throughputs = []
    selected_latency_p999 = []
    selected_latency_p10 = []

    # Iterate over the throughput and latency data to select the maximum value for every four data points
    throughput_values = [max(throughputs.iloc[i][j:j+4]) for j in range(len(x_labels)) if j % 4 == 0]
    selected_throughputs.extend(throughput_values)  # Extend the list

    latency_values_p999 = [correspond_p999_delay.iloc[i][j] for j in range(len(x_labels)) if j % 4 == 0]
    selected_latency_p999.extend(latency_values_p999)

    latency_values_p10 = [correspond_p10_delay.iloc[i][j] for j in range(len(x_labels)) if j % 4 == 0]
    selected_latency_p10.extend(latency_values_p10)

    # Convert the selected lists to NumPy arrays
    selected_throughputs = np.array(selected_throughputs)
    selected_latency_p999 = np.array(selected_latency_p999)
    selected_latency_p10 = np.array(selected_latency_p10)
    print(index_label)
    print(selected_throughputs)
    print(selected_latency_p10)
    print(selected_latency_p999)

    # Create a line plot with the specified color, line style, and label for P999 latency
    ax1.plot(selected_throughputs, selected_latency_p10, label=index_label, 
            marker=properties['marker'], markerfacecolor='none')

    # Create a line plot with the specified color, line style, and label for P10 latency
    ax2.plot(selected_throughputs, selected_latency_p999, label=index_label,
            marker=properties['marker'], markerfacecolor='none')
    ax2.set_yticks([1, 2, 3])


    i += 1

# Set labels and titles for P999 latency subplot
ax1.set_xlabel('Throughputs(Miops)')
ax1.set_ylabel('latency(µs)')
# ax1.set_title('Max Throughputs vs. P10 Latency')

# Set labels and titles for P10 latency subplot
ax2.set_xlabel('Throughputs(Miops)')
ax2.set_ylabel('latency(µs, log scale)')
# ax2.set_title('Max Throughputs vs. P999 Latency')

# Add legend to both subplots
# ax1.legend()
# ax2.legend()
legend = fig.legend(*ax1.get_legend_handles_labels(), bbox_to_anchor=(0.5, 1.01), loc='upper center', ncol=4,framealpha=0, handlelength=2)

# add subplot titles below the figures
ax1.text(0.5, -0.2, '(a) throughputs vs median latency', transform=ax1.transAxes, fontsize=20, va='top', ha='center')
ax2.text(0.5, -0.2, '(b) throughputs vs p999 latency', transform=ax2.transAxes, fontsize=20, va='top', ha='center')


# Show the plot
plt.grid(False)

# Save the plot as a high-resolution PDF
plt.savefig(f'throughput-{filename}.pdf', format='pdf', dpi=300)

# plt.tight_layout()
plt.show()