import csv
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set global font size
mpl.rcParams['font.size'] = 20

# Define file names and letters
file_names = ['load_latency', 'run_latency']

# Read data from CSV and create subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5.8))

for idx, file_name in enumerate(file_names):
    with open(f'{file_name}.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = []
        for row in reader:
            data.append(row)

    # Convert data to lists
    labels = [row[0] for row in data]
    labels = [int(label) / 1000 for label in labels]
    values1 = [float(row[1]) for row in data]
    values2 = [float(row[2]) for row in data]
    values3 = [float(row[3]) for row in data]
    values4 = [float(row[4]) for row in data]

    ax = axes[idx]
    x = range(len(labels))
    width = 0.15
    ax.bar(x, values1, width, label='SepHash', edgecolor='black')
    ax.bar([i + width for i in x], values2, width, label='RACE', edgecolor='black')
    ax.bar([i + 2 * width for i in x], values3, width, label='Plush', edgecolor='black')
    ax.bar([i + 3 * width for i in x], values4, width, label='Clevel', edgecolor='black')

    # Set chart parameters
    ax.set_ylabel('Time (us)')
    ax.set_xlabel('Data Size (thousands)')
    ax.set_xticks([i + 2 * width for i in x])
    ax.set_xticklabels([int(label) for label in labels])
    ax.text(0.02, .99, f'{file_name}', ha='left', va='top', transform=ax.transAxes, fontsize=20)

    # Set y-axis limits to be the same for both subplots
    max_value = max(max(values1), max(values2), max(values3), max(values4))
    ax.set_ylim([0, max_value * 1.2])

# Add text labels to the subplots
# axes[0].text(0.05, 0.95, 'load_latency', ha='left', va='top', transform=axes[0].transAxes, fontsize=20)
# axes[1].text(0.05, 0.95, 'run_latency', ha='left', va='top', transform=axes[1].transAxes, fontsize=20)

# Add legend
axes[0].legend(loc='upper center', bbox_to_anchor=(1.1, 1.15), ncol=4, fontsize=18, framealpha=0, handlelength=.4)

# Adjust the distance between the two subplots
# plt.subplots_adjust(wspace=0.25, top=.915, bottom=.11, left=.07, right=1)
plt.subplots_adjust(wspace=0.25, top=.88, bottom=.11, left=.07, right=1)

# Save chart to PDF
plt.savefig('write_latency.pdf', format='pdf')

# Show chart
plt.show()