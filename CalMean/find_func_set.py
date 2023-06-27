# import numpy as np
# import matplotlib.pyplot as plt

# # Load data from the provided NUM table
# data = np.loadtxt('NUM.txt', dtype=np.int64)

# # Calculate the average value and set err-bound to half of it
# avg = np.mean(data[:, 1])
# err_bound = avg / 2

# # Initialize variables
# base = 0
# cur = 0
# slot_data = []
# base_intervals = []

# # Define a function to update the slot and base values
# def update_slot():
#     global slot_data, base
#     slot_data = []
#     base_intervals.append([inter_start, inter_end, base])
#     base += cur - pred

# # Iterate through the data and update the slot if the error exceeds the bound
# inter_start = 0
# for i in range(len(data)):
#     pred = avg * i + base
#     cur += data[i, 1]
#     error = abs(cur - pred)
#     if error > err_bound:
#         inter_end = i
#         update_slot()
#         pred = avg * i + base
#         error = abs(cur - pred)
#         inter_start = i
#     slot_data.append(data[i, 1])

# # Add the last slot to the list of slots
# base_intervals.append([inter_start, len(data) - 1, base])

# # Print the number of different base values used
# print("Number of different base values: {}".format(len(base_intervals)-1))

# # Plot the function for each base interval
# for interval in base_intervals:
#     start, end, base_value = interval
#     # Calculate the function values for the current base interval
#     x = np.arange(start, end+1)
#     y = avg * x + base_value
    
#     # Plot the function
#     plt.plot(x, y, label="Base = {}".format(base_value))

#     # Add labels and legend to the plot
#     plt.xlabel("Index")
#     plt.ylabel("Value")
#     plt.title("Functions for different base intervals")
#     plt.legend()

# # Show the plot
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Load data from the provided NUM table
data = np.loadtxt('NUM.txt', dtype=np.int64)

# Calculate the average value and set err-bound to half of it
avg = np.mean(data[:, 1])
err_bound = avg / 2

# Initialize variables
base = 0
cur = 0
slot_data = []
base_intervals = []

# Define a function to update the slot and base values
def update_slot():
    global slot_data, base
    slot_data = []
    base_intervals.append([inter_start, inter_end, base])
    base += cur - pred

# Iterate through the data and update the slot if the error exceeds the bound
inter_start = 0
for i in range(len(data)):
    pred = avg * i + base
    cur += data[i, 1]
    error = abs(cur - pred)
    if error > err_bound:
        inter_end = i
        update_slot()
        pred = avg * i + base
        error = abs(cur - pred)
        inter_start = i
    slot_data.append(data[i, 1])

# Add the last slot to the list of slots
base_intervals.append([inter_start, len(data) - 1, base])

# Print the number of different base values used
num_base_intervals = len(base_intervals) - 1
print("Number of different base values: {}".format(num_base_intervals))

# Plot the function for each base interval
num_intervals_to_plot = min(5, num_base_intervals)
for i in range(num_intervals_to_plot):
    interval = base_intervals[i]
    start, end, base_value = interval
    # Calculate the function values for the current base interval
    x = np.arange(start, end+1)
    y = avg * x + base_value
    
    # Plot the function
    plt.plot(x, y, label="Base = {}".format(base_value))

    # Add labels and legend to the plot
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.title("Functions for different base intervals (Top 5)")
    plt.legend()

# Show the plot
plt.show()