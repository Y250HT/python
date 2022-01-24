# 随机开柜码
# 大型超市为顾客提供了寄存包裹的保管箱，放入随身包裹时生成一个取件码发给用户，
# 用户凭取件码自行提取包裹。取件码的字符包括：数字 0 - 9 和字母 A、B、C、D、E、
# F、G、H、I、J。每次从以上字符串 'ABCDEFGHIJ0123456789' 中随机取一个字符，重复
# 6 次， 生成一个形如 “9I16A4” 的取件码，各字符的使用次数无限制。随机数种
# 子 n 由用户输入。
# 输入: 5
#输出: 9I16A4

#方法一
# import random
# n = input()
# random.seed(int(n)) # 随机数种子 n 由用户输入
# Sn = '' # 空字符串
# characters = 'ABCDEFGHIJ0123456789'
# for i in range(6):
#     Sn = Sn + random.choice(characters) # 生成的字符连接到字符串上
#     #choice()方法从指定序列中返回一个随机选择的元素，该序列可以是字符串，范围，列表，元组或任何其他种类的序列
# print(Sn)

#方法二
import random
n = eval(input())
random.seed(n)
str = "ABCDEFGHIJ0123456789"
for i in range(6):
    print("{}".format(random.choice(str)),end = "")
    ##choice()方法从指定序列中返回一个随机选择的元素，该序列可以是字符串，范围，列表，元组或任何其他种类的序列