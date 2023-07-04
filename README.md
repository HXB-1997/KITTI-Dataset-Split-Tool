# 划分KITTI数据集
- 划分来源：```https://github.com/anshulpaigwar/Frustum-Pointpillars/tree/main/second/data```
- 个人台式机路径：/home/han/Desktop/hxb_projects/kitti_split_tool/split_kitti.py
## 脚本
- random_split.py
    - 功能：随机将7480张按照7：1.5：1.5分三组,输出三组图片序号txt文件
- split_kitti.py
    - 功能：根据random_split.py划分的序号将数据集图片和标签分组保存
    - 注意：
        - 修改路径：
            ```
            # 源文件夹路径
            source_folder = '/home/han/Desktop/hxb_projects/DataSets/KITTI/3D_det/training/'

            # 目标文件夹路径
            destination_folder = '/home/han/Desktop/hxb_projects/kitti_split_tool/train_val_test-Datasets/test/'

            # 标签TXT文件
            label_txt = '/home/han/Desktop/hxb_projects/kitti_split_tool/train_val_test-Datasets/test.txt'
            ```
        - 每个子文件夹手动新建images和labels文件夹