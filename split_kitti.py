import os
import shutil

# 源文件夹路径
source_folder = '/home/han/Desktop/hxb_projects/DataSets/KITTI/3D_det/training/'

# 目标文件夹路径
destination_folder = '/home/han/Desktop/hxb_projects/kitti_split_tool/val/'

# 从train.txt文件中读取序号列表
with open('split_rule/val.txt', 'r') as file:
    indexes = [line.strip() for line in file]

# 遍历序号列表
for index in indexes:
    # 构建源文件路径和目标文件路径
    source_png_file = os.path.join(source_folder+'image_2', index + '.png')
    destination_file = os.path.join(destination_folder+'images', index + '.png')

    # 复制PNG文件到目标文件夹
    shutil.copyfile(source_png_file, destination_file)

    # 构建源文件路径和目标文件路径（对应的TXT文件）
    source_txt_file = os.path.join(source_folder+'label_2', index + '.txt')
    destination_file = os.path.join(destination_folder+'labels', index + '.txt')

    # 复制TXT文件到目标文件夹
    shutil.copyfile(source_txt_file, destination_file)
