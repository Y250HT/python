# 字符串加密
# 用户在一行中输入一个包括大小写字母和数字的字符串，编程将其中的大写字母用该字母后的第5个字母替代
# 小写字母用该字母后的第 3 个字符替代，其他字符原样输出，
# 实现字符串加密。

#方法一存在一定的问题 对于如果输入z则会导致出现符号问题
# str = input()
# t = ""
# for c in str:
#     if 'a' <= c <= 'z':
#         t += chr(ord(c) + 3)
#         #a->97 z->122
#         #ord() 返回对应的ASCII数值 返回值是对应的十进制整数
#     elif 'A' <= c <= 'Z':
#         t += chr(ord(c) + 5)
#         #chr()返回值是当前整数对应的ASCII字符
#         #A->65  Z->90
#     else:
#         t+=c
# print(t)

str = input()
t = ""
for c in str:
    if c.islower():   #判断是否为小写字母
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )  #利用取模运算进行封闭循环起来，将a和z进行连接起来
    elif c.isupper():   #判断是否为大写字母
        t += chr( ord('A') + ((ord(c)-ord('A')) + 5 )%26 )
    else:
        t += c
print(t)

#方法二解决了方法一出现的问题
