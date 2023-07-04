import random

# 生成从000000到007480的数字列表
numbers = list(range(7481))

# 按照比例计算每组的数量
total = len(numbers)
group1_count = int(total * 0.7)
group2_count = int(total * 0.15)
group3_count = total - group1_count - group2_count

# 随机打乱数字列表
random.shuffle(numbers)

# 将数字分组
group1 = numbers[:group1_count]
group2 = numbers[group1_count : group1_count + group2_count]
group3 = numbers[group1_count + group2_count:]

# 将每组的数字保存到对应的txt文件中
with open("./train_val_test/train.txt", "w") as file:
    for number in group1:
        file.write("{:06d}\n".format(number))

with open("./train_val_test/val.txt", "w") as file:
    for number in group2:
        file.write("{:06d}\n".format(number))

with open("./train_val_test/test.txt", "w") as file:
    for number in group3:
        file.write("{:06d}\n".format(number))
