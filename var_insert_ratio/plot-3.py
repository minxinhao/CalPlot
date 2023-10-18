import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.size'] = 20
mpl.rcParams['axes.edgecolor'] = 'black'  # 设置边框颜色为黑色

# Read data
data = {
    "1:9": {
        "SepHash": [33324.55, 23393.16, 34219.85, 32528.72],
        "RACE": [38745.28, 38392.86, 38126.79, 43430.29],
        "CLevel": [5636.42, 5394.79, 8376.28, 13154.03],
        "Plush": [5179.04, 4454.97, 5667.68, 8758.2]
    },
    "3:7": {
        "SepHash": [24741.47, 14790.61, 23668.89, 21464.19],
        "RACE": [28256.879999999997, 30293.43, 25652.67, 21373.07],
        "CLevel": [7011.33, 6740.07, 6015.09, 6835.85],
        "Plush": [5276.08, 4836.88, 4872.92, 3616.72]
    },
    "5:5": {
        "SepHash": [14925.88, 17194.45, 18453.72, 13123.39],
        "RACE": [2263.71, 1770.82, 1468.3, 928.4],
        "CLevel": [6330.85, 6943.72, 7544.2, 7936.3],
        "Plush": [5024.1, 4906.8, 4316, 3858]
    },
    "7:3": {
        "SepHash": [16315.32, 11457.41, 16415.57, 12931.95],
        "RACE": [2198.6, 1007.56, 645.77, 366.55],
        "CLevel": [5540.13, 5540.63, 5859.08, 6729.94],
        "Plush": [4966.56, 3236.74, 2755.7, 2419.1]
    },
    "9:1": {
        "SepHash": [16154.81, 14006.63, 11138.43, 15787.39],
        "RACE": [2181.15, 643.25, 539.56, 431.49],
        "CLevel": [5001.69, 4655.24, 6300.84, 12209.47],
        "Plush": [5738.42, 2930.96, 2720.24, 2322.62]
    }
}

# Extract indexes and ratios
indexes = list(data[next(iter(data))].keys())  
ratios = list(data.keys())

# Create values array
values = np.zeros((len(ratios), len(indexes)))  

# Fill values array
for i, ratio in enumerate(ratios):
  for j, index in enumerate(indexes):
    values[i, j] = max(data[ratio][index])/1000
    
# Set figure size and adjust subplots  
plt.figure(figsize=(7, 5.8))
plt.subplots_adjust(wspace=0.1, top=.9, bottom=.11, left=.111, right=.99)

# Plot bars
x = np.arange(len(ratios))
width = 0.2  
for i, index in enumerate(indexes):
  plt.bar(x - 1.5*width + i*width, values[:,i], width,label=index)
  
# Add labels and legends  
plt.xlabel("Read/Write Ratio")
plt.xticks(x, ratios)  
plt.ylabel('Throughput (Mops/s)')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=18, framealpha=0, handlelength=.4)

# Save figure
plt.savefig('var_insert_ratio.pdf')

# Show plot
plt.show()