import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
colors_markers = {'RACE': {'color': 'b', 'marker': 'o'}, 
                  'SepHash': {'color': 'g', 'marker': 's'}, 
                  'Plush': {'color': 'r', 'marker': 'D'}, 
                  'CLevel': {'color': 'c', 'marker': 'v'}}

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))

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
    ax.plot(selected_throughputs, selected_p10_latency, label=index_label, color=properties['color'],
            marker=properties['marker'], markerfacecolor='none', markeredgecolor=properties['color'])
    i+=1

# Set labels and title
ax.set_xlabel('Throughputs (Max of Every 4 Points)')
ax.set_ylabel(delay_name)
ax.set_title(f'Line Plot of Max Throughputs vs. {delay_name}')

# Add legend
ax.legend()

# Show the plot
plt.grid(False)

# Save the plot as a high-resolution PDF
plt.savefig(f'throughput-{delay_name}.pdf', format='pdf', dpi=300)

plt.tight_layout()
plt.show()
