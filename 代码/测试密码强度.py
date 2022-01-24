str1 = input()
x,y,p,q=0,0,0,0
for i in str1:
    if 65<=ord(i)<=96:
        x = 1
    elif 97<=ord(i)<=122:
        y = 1
    elif 48<=ord(i)<=57:
        p = 1
    else:
        q = 1
s = x + y + p + q
if len(str1)<8 :
    print("弱")
else:
    if s < 2:
        print("弱")
    elif s == 2:
        print("中")
    elif s == 3:
        print("强")
    else:
        print("极强")