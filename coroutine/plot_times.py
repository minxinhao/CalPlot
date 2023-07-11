# import csv
# import matplotlib.pyplot as plt

# data = {
#     "SepHash":[1,1.649545211,2.049491707,2.233386838,1,1.571723394,1.843215771,1.950223317,1,1.429970572,1.554625713,1.557545521,1,1.315728515,1.532296288,1.529480943,1,1.101575981,1.223124928,1.422682043,1,1.215004204,1.325387717,1.600027004,1,1.64170426,1.526272001,1.53263817,1,1.655909331,1.584558502,1.802544594],
#     "RACE":[1,1.823796185,2.418700814,2.891023076,1,1.767585819,2.177546427,2.394625774,1,1.659294389,1.765579293,1.82687705,1,1.349088056,1.35847365,1.176617264,1,0.977577175,0.71140278,0.559932732,1,0.729003825,0.32008149,0.198636288,1,0.277733771,0.148943772,0.092203769,1,0.300946829,0.163157635,0.125590739],
#     "Clevel":[1,1.739374918,2.27069439,2.936184124,1,1.825037821,1.819591528,2.189712557,1,1.737554293,2.165552957,2.42705201,1,1.477013739,1.916042458,2.04029252,1,1.476420579,1.528385746,1.701904442,1,1.591270043,1.599841384,2.271618997,1,1.516820872,1.820899947,1.550182921,1,1.588150164,1.645039699,1.685923042],
#     "Plush":[1,1.633200623,2.025099533,2.290635278,1,1.544886247,1.898134864,2.269522443,1,1.424852526,1.673506027,1.628622724,1,1.35191358,1.691975309,1.555864198,1,1.497560976,1.297560976,1.053658537,1,0.408214044,0.320390735,0.357475881,1,0.377643201,0.346577222,0.291179555,1,0.482441586,0.412238374,0.335155419],
# }

# # 生成横坐标标签
# sequence = [1]
# while sequence[-1] < 128:
#     sequence.append(sequence[-1] * 2)

# xticklabels = ["0-0",]
# for i in sequence:
#     for j in range(4):
#         xticklabels.append(f"{i}-{j+1}")

# # 绘制柱状图
# fig, ax = plt.subplots()
# bar_width = 0.2
# for i, (index, values) in enumerate(data.items()):
#     x_values = [j + i * bar_width for j in range(1, len(values) + 1)]
#     ax.bar(x_values, values, width=bar_width, label=index)
# ax.set_xlabel("Number of coroutines")
# ax.set_ylabel("Performance")
# ax.set_title("Performance vs. Number of coroutines")
# ax.set_xticks([j + 1.5 * bar_width for j in range(len(xticklabels))])
# ax.set_xticklabels(xticklabels)
# ax.legend()
# plt.show()
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20
# outfilename = "plot-times-insert.pdf"
outfilename = "plot-times-search.pdf"
# insert
# data = {
#     "SepHash":[1.649545211, 2.049491707, 2.233386838, 1.315728515, 1.532296288, 1.529480943, 1.655909331, 1.584558502, 1.802544594],
#     "RACE":[1.823796185, 2.418700814, 2.891023076, 1.349088056, 1.35847365, 1.176617264, 0.300946829, 0.163157635, 0.125590739],
#     "Clevel":[1.739374918, 2.27069439, 2.936184124, 1.477013739, 1.916042458, 2.04029252, 1.588150164, 1.645039699, 1.685923042],
#     "Plush":[1.633200623, 2.025099533, 2.290635278, 1.35191358, 1.691975309, 1.555864198, 0.482441586, 0.412238374, 0.335155419],
# }
# search
data = {
    "SepHash":[1.915469543, 2.619293235, 3.063174048, 1.639246174, 2.001662973, 1.716007048, 0.702283636, 1.088383091, 0.845186193],
    "RACE":[1.900278255, 2.811768557, 3.380268434, 1.841648207, 2.002495324, 1.702681504, 0.670149795, 0.93609183, 1.163548768],
    "Clevel":[1.694311412, 1.872912043, 3.140520967, 1.508175014, 1.844559585, 1.700364613, 1.180887259, 1.156313032, 1.188632576],
    "Plush":[1.94081381, 2.2, 3.226880395, 2.050999747, 2, 2.046317388, 0.952256103, 1.1, 1.165194124],
}

# 设置横坐标标签
xticklabels = ["1-2", "1-3", "1-4", "16-2", "16-3", "16-4", "128-2", "128-3", "128-4"]

# 绘制柱状图
plt.figure(figsize=(12, 6.7))
plt.subplots_adjust(wspace=0.1, top=.9,left=.1,right=.99)
bar_width = 0.2
for i, (index, values) in enumerate(data.items()):
    x_values = [j + i * bar_width for j in range(len(values))]
    # plt.bar(x_values, values, width=bar_width, label=index)
    plt.bar(x_values, values, width=bar_width, label=index, edgecolor='black')

plt.xlabel("Number of threads-coroutines")  
plt.ylabel("Performance Improvement Times")       
plt.xticks([j + 1.5 * bar_width for j in range(len(xticklabels))],xticklabels)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=20, framealpha=0, handlelength=.8)
plt.savefig(outfilename, format='pdf')
plt.show()