import matplotlib.pyplot as plt
import matplotlib as mpl

# Set global font size
mpl.rcParams['font.size'] = 14

# 设置横坐标标签
xticklabels = ["1-2", "1-3", "1-4", "16-2", "16-3", "16-4", "128-2", "128-3", "128-4"]

# insert
data_insert = {
    "SepHash":[1.649545211, 2.049491707, 2.233386838, 1.315728515, 1.532296288, 1.529480943, 1.655909331, 1.584558502, 1.802544594],
    "RACE":[1.823796185, 2.418700814, 2.891023076, 1.349088056, 1.35847365, 1.176617264, 0.300946829, 0.163157635, 0.125590739],
    "Clevel":[1.739374918, 2.27069439, 2.936184124, 1.477013739, 1.916042458, 2.04029252, 1.588150164, 1.645039699, 1.685923042],
    "Plush":[1.633200623, 2.025099533, 2.290635278, 1.35191358, 1.691975309, 1.555864198, 0.482441586, 0.412238374, 0.335155419],
}

# search
data_search = {
    "SepHash":[1.915469543, 2.619293235, 3.063174048, 1.639246174, 2.001662973, 1.716007048, 0.702283636, 1.088383091, 0.845186193],
    "RACE":[1.900278255, 2.811768557, 3.380268434, 1.841648207, 2.002495324, 1.702681504, 0.670149795, 0.93609183, 1.163548768],
    "Clevel":[1.694311412, 1.872912043, 3.140520967, 1.508175014, 1.844559585, 1.700364613, 1.180887259, 1.156313032, 1.188632576],
    "Plush":[1.94081381, 2.2, 3.226880395, 2.050999747, 2, 2.046317388, 0.952256103, 1.1, 1.165194124],
}

# 创建一个包含两个子图的图形
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 5.8))

# 创建 insert 的子图
axs[0].set_title('Insert Performance Times')
for i, (index, values) in enumerate(data_insert.items()):
    x_values = [j + i * 0.2 for j in range(len(values))]
    axs[0].bar(x_values, values, width=0.2, label=index)
axs[0].set_xlabel('Number of threads-coroutines')
axs[0].set_ylabel('Performance Times')
axs[0].set_xticks([j + 0.3 for j in range(len(xticklabels))])
axs[0].set_xticklabels(xticklabels)
axs[0].legend(loc='upper center', bbox_to_anchor=(1.1, 1.2), ncol=4, fontsize=20, framealpha=0, handlelength=.8)

# 创建 search 的子图
axs[1].set_title('Search Performance Times')
for i, (index, values) in enumerate(data_search.items()):
    x_values = [j + i * 0.2 for j in range(len(values))]
    axs[1].bar(x_values, values, width=0.2, label=index)
axs[1].set_xlabel('Number of threads-coroutines')
axs[1].set_ylabel('Performance Times')
axs[1].set_xticks([j + 0.3 for j in range(len(xticklabels))])
axs[1].set_xticklabels(xticklabels)
# axs[1].legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=10, framealpha=0, handlelength=.8)

# 调整子图之间的距离

# plt.subplots_adjust(wspace=0.4)
plt.subplots_adjust(wspace=0.2, top=.88,bottom=.1,left=.07,right=.98)
plt.savefig('plot_times.pdf', format='pdf')

plt.show()

