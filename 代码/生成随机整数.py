# 生成随机整数
# 以 123 为随机数种子，随机生成 10 个在 1 到 999（含）之间的随机数，以逗号分隔，
# 打印输出，请补充横线处代码。提示代码如下：
# import random
# ____①____
# for i in range(____②____):
# print(____③____, end=",")
# 输入：无
# 输出："54,275,90,"

import random
random.seed(123)
for i in range(10):
    print(random.randint(1,999), end=",")