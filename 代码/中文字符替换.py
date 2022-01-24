num=input("请输入一个数字：")
s = "〇一二三四五六七八九"
n=""
i=0
while i<len(num):
    n=n+s[eval(num[i])]
    i+=1
print(n)
