import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# Read the data from the CSV file
data = pd.read_csv('insert-latency.csv', delimiter=',', index_col=0, skip_blank_lines=True)

# Get the x labels from the first row of delay_data
x_labels = list(data.columns)

# Extract the throughput and P10 latency data
delay_name = 'P999 latency'
# delay_name = 'P10 latency'
throughputs = data.loc['throughputs'].astype(np.float64)
p10_latency = data.loc[delay_name].astype(np.float64)
if delay_name == "P999 latency" or delay_name == "P99 latency" or delay_name == "P9999 latency" :
    p10_latency = np.log(p10_latency)

# Create a dictionary to map index labels to colors and markers
colors_markers = {'SepHash': {'color': 'g', 'marker': 's'}, 
                  'RACE': {'color': 'b', 'marker': 'o'}, 
                  'Plush': {'color': 'r', 'marker': 'D'}, 
                  'CLevel': {'color': 'c', 'marker': 'v'}}

# Create a figure and axis for the plot
plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.1, top=.98, bottom=0.12, left=0.15, right=0.99)

# Iterate over each index label (RACE, SepHash, Plush, CLevel)
i = 0
for index_label, properties in colors_markers.items():
    # Create lists to store the selected data
    selected_throughputs = []
    selected_p10_latency = []

    # Iterate over the throughput and P10 latency data to select the maximum value for every four data points

    throughput_values = [max(throughputs.iloc[i][j:j+4]) for j in range(len(x_labels)) if j % 4 == 0]
    selected_throughputs.extend(throughput_values)  # Extend the list

    p10_latency_values = [p10_latency.iloc[i][j] for j in range(len(x_labels)) if j % 4 == 0]
    selected_p10_latency.extend(p10_latency_values)

    # Convert the selected lists to NumPy arrays
    selected_throughputs = np.array(selected_throughputs)
    selected_p10_latency = np.array(selected_p10_latency)

    # Create a line plot with the specified color, line style, and label
    # ax.plot(selected_throughputs, selected_p10_latency, label=index_label, color=properties['color'], marker=properties['marker'])
    plt.plot(selected_throughputs, selected_p10_latency, label=index_label, color=properties['color'],
            marker=properties['marker'], markerfacecolor='none', markeredgecolor=properties['color'])
    i+=1

# Set labels and title
plt.xlabel('Throughputs(iops)')
# plt.set_ylabel(delay_name)
if delay_name == "P10 latency":
    plt.ylabel('latency(us)')
    # plt.title(f'Max Throughputs vs. Median Latency')
elif delay_name == "P999 latency" :
    plt.ylabel('log(latency)(us)')
    # plt.title(f'Max Throughputs vs. P999 Latency')
else :
    plt.ylabel('latency(us)')
    # plt.title(f'Max Throughputs vs. {delay_name}')



# Add legend
plt.legend()

# Show the plot
plt.grid(False)

# Save the plot as a high-resolution PDF
plt.savefig(f'throughput-{delay_name}.pdf', format='pdf', dpi=300)

plt.tight_layout()
plt.show()
