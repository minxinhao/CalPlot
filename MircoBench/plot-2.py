from pdf2image import convert_from_path
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# Convert the first page of 'micro_bench_insert.pdf' to an image
images1 = convert_from_path('micro_bench_insert.pdf')
images2 = convert_from_path('ycsb_search.pdf')
images3 = convert_from_path('var_insert_ratio.pdf')
img1 = images1[0]
img2 = images2[0]
img3 = images3[0]

# Create a figure object and set the size
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(19, 5.8))

# Set the border color for each subplot
border_color = 'black'

# Display the first image with darkened border
ax1.imshow(img1)
ax1.axis('off')  # Remove the axes
ax1.spines['left'].set_color(border_color)  # Set left border color
ax1.spines['right'].set_color(border_color)  # Set right border color
ax1.spines['top'].set_color(border_color)  # Set top border color
ax1.spines['bottom'].set_color(border_color)  # Set bottom border color
ax1.text(0.5, -0.1, '(a) Insert Performance', transform=ax1.transAxes, ha='center')  # Add the subfigure name

# Display the second image with darkened border
ax2.imshow(img2)
ax2.axis('off')  # Remove the axes
ax2.spines['left'].set_color(border_color)  # Set left border color
ax2.spines['right'].set_color(border_color)  # Set right border color
ax2.spines['top'].set_color(border_color)  # Set top border color
ax2.spines['bottom'].set_color(border_color)  # Set bottom border color
ax2.text(0.5, -0.1, '(b) Search Performance', transform=ax2.transAxes, ha='center')  # Add the subfigure name

# Display the third image with darkened border
ax3.imshow(img3)
ax3.axis('off')  # Remove the axes
ax3.spines['left'].set_color(border_color)  # Set left border color
ax3.spines['right'].set_color(border_color)  # Set right border color
ax3.spines['top'].set_color(border_color)  # Set top border color
ax3.spines['bottom'].set_color(border_color)  # Set bottom border color
ax3.text(0.5, -0.1, '(c) Hybrid Workloads', transform=ax3.transAxes, ha='center')  # Add the subfigure name

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.001, top=1.1, bottom=.0001, left=.01, right=.99)

# Save the combined figure with darkened borders
plt.savefig('micro_bench.pdf', bbox_inches='tight', pad_inches=0.1, edgecolor=border_color, transparent=True)

# Display the combined figure
plt.show()