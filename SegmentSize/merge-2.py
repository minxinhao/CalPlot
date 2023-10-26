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
pdf_files = ["CurSegment-Size.pdf","MainSegment-Size.pdf"]


# 图例标签
legend_labels = ['insert', 'search']

# 创建一个子图对象，并设置大小和布局
fig, axs = plt.subplots(1,2, figsize=(7, 3))

# 遍历每个PDF文件和对应的子图对象
i = 0
for pdf_file, ax in zip(pdf_files, axs):
    # 提取PDF文件中的图像
    image = extract_image_from_pdf(pdf_file)
    
    # 显示图像
    ax.imshow(image)
    ax.axis('off')  # 移除坐标轴
    if i == 0:
      ax.text(0.5, -0.05, '(a) Impact of CurSegment Size', transform=ax.transAxes, fontsize=12, va='top', ha='center')
    else:
      ax.text(0.5, -0.05, '(b) Impact of MainSegment Size', transform=ax.transAxes, fontsize=12, va='top', ha='center')
    i+=1


# 调整子图之间的间距，增加额外的空白间距
plt.subplots_adjust(wspace=0.01, top=1, bottom=.1, left=.01, right=.99)


# 在顶部生成共享的图例
fig.legend(legend_labels, loc='center', bbox_to_anchor=(.4, .4), ncol=len(pdf_files), fontsize=20, framealpha=0, handlelength=.4)

# 保存合并后的图像
plt.savefig(f'Segment-Size.pdf',format='pdf',dpi=300)

# 显示合并后的图像
plt.show()

