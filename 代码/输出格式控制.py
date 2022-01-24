# 输出格式控制
# 获得用户的输入当作对齐模式，用户输入：左、右、中，分别表示：左对齐、右对
# 齐和居中对齐，以 * 作为填充符号，30 字符宽度输出 PYTHON 字符串。请完善代码。
# m = input("请输入对齐模式：")
# s = "PYTHON"
# if m =="右":
#  m = ">"
# elif m =="中":
#  m = "^"
# else:
#  m = "<"
# print("{_____①_____}".format(_____②_____))

#方法一
m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    m = ">"
elif  m =="中":
    m = "^"
else:
    m = "<"
print("{1:*{0}30}".format(m,s))  #用*进行补齐 {0}对应m 1外层对应s

#方法二
m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    m = ">"
    print("{0:*>30}".format(s))
elif  m =="中":
    m = "^"
    print("{0:*^30}".format(s))
else:
    m = "<"
    print("{0:*<30}".format(s))

#方法三
m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    print(s.rjust(30,'*'))
elif  m =="中":
    print(s.center(30,'*'))
else:
    print(s.ljust(30,'*'))