import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# Read the data from the CSV file
filename = 'search-latency'
# filename = 'insert-latency'
# data = pd.read_csv(filename, delimiter=',', index_col=0, skip_blank_lines=True)
data = pd.read_csv(f'{filename}.csv', delimiter=',', index_col=0, skip_blank_lines=True)

# Set the selected delay names
# selected_delays = ['P10 latency', 'P999 latency']
selected_delays = ['P10 latency', 'P9999 latency']
index_label = ['SepHash', 'RACE', 'CLevel','Plush']

# Get the x labels from the first row of delay_data
x_labels = list(data.columns)

# Define the indices you want to select (0, 4, 8, ...)
selected_indices = list(range(0, len(x_labels), 4))

# Select corresponding x_labels and delay_data based on selected indices
x_labels = [1, 2, 4, 8, 16, 32, 64, 128]

# Define the width of each bar
bar_width = 0.2  # Adjust this value to change the gap between bars

# Create a new figure for the subplots
fig, axes = plt.subplots(nrows=1, ncols=len(selected_delays), figsize=(12, 5.8))

# Iterate over each delay
for delay_index, delay_name in enumerate(selected_delays):
    print(delay_index,delay_name)
    # Get the delay data for each row starting from the second row (index 1)
    delay_data = data.loc[delay_name][0:].astype(np.float64)
    # Check if delay_name is "P999 latency" and apply log transformation
    if delay_name == "P999 latency" or delay_name == "P99 latency" or delay_name == "P9999 latency":
        delay_data = np.log10(delay_data)

    # Iterate over each row in delay_data
    selected_delay_data = []
    for i in range(len(delay_data)):
        # Keep the first element and every fourth element starting from the second element
        selected_delay_data.append(delay_data.iloc[i][selected_indices])

    # Convert the selected_delay_data list to a NumPy array
    selected_delay_data_array = np.array(selected_delay_data)
    print(selected_delay_data_array)
    max_value = np.max(selected_delay_data)
    max_value = max_value * 1.1

    # Adjust the position of the subplot based on the delay index
    ax = axes[delay_index]

    # Create an array of x values using numpy.arange to ensure they are numeric
    x_values = np.arange(len(x_labels))

    # Adjust x_values to offset each set of bars
    x_values_race = x_values - bar_width * 1.5
    x_values_sephash = x_values - bar_width * 0.5
    x_values_plush = x_values + bar_width * 0.5
    x_values_clevel = x_values + bar_width * 1.5

    # Plot the data as a bar chart for each index_label
    ax.bar(x_values_race, list(selected_delay_data[0]), width=bar_width, label=index_label[0])
    ax.bar(x_values_sephash, list(selected_delay_data[1]), width=bar_width, label=index_label[1])
    ax.bar(x_values_plush, list(selected_delay_data[2]), width=bar_width, label=index_label[2])
    ax.bar(x_values_clevel, list(selected_delay_data[3]), width=bar_width, label=index_label[3])

    # Set y-axis limit to ensure consistency across all graphs
    ax.set_ylim(0, max_value)

    # Set xticks and labels
    ax.set_xticks(x_values)
    ax.set_xticklabels(x_labels)

    # Set labels and title
    ax.set_xlabel('Number of Threads')
    if delay_name == "P10 latency":
        ax.set_ylabel('Latency (us)')
        ax.text(0.5, -0.2, '(a) Median Latency', transform=ax.transAxes, fontsize=20, va='top', ha='center')
    elif delay_name == "P999 latency" or delay_name == "P9999 latency":
        ax.set_ylabel('Log Latency (us)')
        ax.text(0.5, -0.2, '(b) P999 Latency', transform=ax.transAxes, fontsize=20, va='top', ha='center')

    # Set the number of y-axis ticks (adjust as needed)
    ax.set_yticks(np.linspace(0, float(max_value), num=6, dtype=int))  # Ensure the tick values are integers

    # Add legend
    # ax.legend()

plt.subplots_adjust(wspace=0.3, top=.9,bottom=.2,left=.08,right=.99)
fig.legend(index_label,loc='upper center', bbox_to_anchor=(0.5, 1.02), ncol=4, fontsize=16,framealpha=0, handlelength=.4)

# Save the plot as a high-resolution PDF
plt.savefig(f'{filename}-combined.pdf', format='pdf', dpi=300)

# Show the plot
# plt.tight_layout()
plt.show()