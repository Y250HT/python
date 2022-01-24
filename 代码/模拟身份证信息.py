# 模拟身份证信息
# 输入一个模拟身份证号，将其中的生日信息与性别输出。
# 如果输入证件位数不是 18 位，输出”ERROR“。
# 本题中判断身份证第 17 位是奇数为男性，偶数为女性。7 到 14 位为出生日期

c=input()
if len(c)!=18:
    print("ERROR")
else:
    print("{}年{}月{}日".format(c[6:10],c[10:12],c[12:14]))
    #根据身份证号的倒数第二位数判断性别
    if int(c[-2])%2==1:
        print("男")
    else:
        print("女")