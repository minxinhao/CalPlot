from pdf2image import convert_from_path
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体大小
mpl.rcParams['font.size'] = 20

# 从PDF文件中提取图像
def extract_image_from_pdf(pdf_file):
    images = convert_from_path(pdf_file)
    return images[0] if images else None

# PDF文件名列表
pdf_files = [
    "insert-latency-P10 latency.pdf",
    "insert-latency-P999 latency.pdf",
    "search-latency-P10 latency.pdf",
    "search-latency-P9999 latency.pdf"
]

# 图例标签
legend_labels = ['RACE', 'SepHash', 'Plush', 'CLevel']

# 创建一个子图对象，并设置大小和布局
fig, axs = plt.subplots(1, len(pdf_files), figsize=(19, 4))

# 遍历每个PDF文件和对应的子图对象
for pdf_file, ax in zip(pdf_files, axs):
    # 提取PDF文件中的图像
    image = extract_image_from_pdf(pdf_file)
    
    # 显示图像
    ax.imshow(image)
    ax.axis('off')  # 移除坐标轴

# 调整子图之间的间距，增加额外的空白间距
plt.subplots_adjust(wspace=0.01, top=1.2, bottom=-.2, left=.01, right=.99)


# 在顶部生成共享的图例
fig.legend(legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=len(pdf_files), fontsize=20, framealpha=0, handlelength=.4)

# 保存合并后的图像
plt.savefig('all-latency.pdf')

# 显示合并后的图像
plt.show()