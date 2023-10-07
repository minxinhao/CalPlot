import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the CSV file
data = pd.read_csv('insert-latency.csv', delimiter=',', index_col=0, skip_blank_lines=True)

# Set the selected delay names
selected_delays = ['P10 latency', 'median latency', 'P9999 latency']
index_label = ['RACE', 'SepHash', 'Plush', 'CLevel']

# Get the x labels from the first row of delay_data
x_labels = list(data.columns)

# Define the width of each bar
bar_width = 0.2  # Adjust this value to change the gap between bars

# Iterate over each delay
for i, delay_name in enumerate(selected_delays):
    # Get the delay data for each row starting from the second row (index 1)
    delay_data = data.loc[delay_name][0:].astype(np.float64)
    print(delay_data)
    # Check if delay_name is "P999 latency" and apply log transformation
    if delay_name == "P999 latency" or delay_name == "P99 latency" or delay_name == "P9999 latency" :
        delay_data = np.log(delay_data)

    max_value = delay_data.max().max()
    print(max_value)
    max_value = max_value * 1.1

    # Create a new figure for each delay
    plt.figure(figsize=(10, 6))

    # Create an array of x values using numpy.arange to ensure they are numeric
    x_values = np.arange(len(x_labels))

    # Adjust x_values to offset each set of bars
    x_values_race = x_values - bar_width * 1.5
    x_values_sephash = x_values - bar_width * 0.5
    x_values_plush = x_values + bar_width * 0.5
    x_values_clevel = x_values + bar_width * 1.5

    # Plot the data as a bar chart for each index_label
    plt.bar(x_values_race, list(delay_data.iloc[0]), width=bar_width, label=index_label[0])
    plt.bar(x_values_sephash, list(delay_data.iloc[1]), width=bar_width, label=index_label[1])
    plt.bar(x_values_plush, list(delay_data.iloc[2]), width=bar_width, label=index_label[2])
    plt.bar(x_values_clevel, list(delay_data.iloc[3]), width=bar_width, label=index_label[3])

    # Set y-axis limit to ensure consistency across all graphs
    plt.ylim(0, max_value)

    # Set xticks and labels
    plt.xticks(x_values, x_labels, rotation=45)

    # Set labels and title
    plt.xlabel('Configuration')
    plt.ylabel(delay_name)
    plt.title(f'{delay_name} for Different Configurations')

    # Set the number of y-axis ticks (adjust as needed)
    plt.yticks(np.linspace(0, float(max_value), num=6, dtype=int))  # Ensure the tick values are integers

    # Add legend
    plt.legend()

    # Save the plot as a high-resolution PDF
    plt.savefig(f'{delay_name}.pdf', format='pdf', dpi=300)

    # Show the plot (optional)
    plt.tight_layout()
    plt.show()
