
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the CSV file
data = pd.read_csv('insert-latency.csv', delimiter=',', index_col=0, skip_blank_lines=True)

# Get the x labels from the first row of delay_data
x_labels = list(data.columns)

# Extract the throughput and P10 latency data
throughputs = data.loc['throughputs'].astype(np.float64)
p10_latency = data.loc['P10 latency'].astype(np.float64)

# Create a dictionary to map index labels to colors
colors = {'RACE': 'b', 'SepHash': 'g', 'Plush': 'r', 'CLevel': 'c'}

# Iterate over each index label (RACE, SepHash, Plush, CLevel)
for i, index_label in enumerate(colors.keys()):
    # Create lists to store the selected data
    selected_throughputs = []
    selected_p10_latency = []

    # Iterate over the throughput and P10 latency data to select the maximum value for every four data points
    # for i in range(len(throughputs)):
    throughput_values = [max(throughputs.iloc[i][j:j+4]) for j in range(len(x_labels)) if j % 4 == 0]
    selected_throughputs.extend(throughput_values)  # Extend the list

    p10_latency_values = [p10_latency.iloc[i][j] for j in range(len(x_labels)) if j % 4 == 0]
    selected_p10_latency.extend(p10_latency_values)

    # Convert the selected lists to NumPy arrays
    selected_throughputs = np.array(selected_throughputs)
    selected_p10_latency = np.array(selected_p10_latency)

    # Create a scatter plot with the specified color and label
    plt.scatter(selected_throughputs, selected_p10_latency, alpha=0.5, c=colors[index_label], label=index_label)

# Set labels and title
plt.xlabel('Throughputs (Max of Every 4 Points)')
plt.ylabel('P10 Latency')
plt.title('Scatter Plot of Max Throughputs vs. P10 Latency')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
