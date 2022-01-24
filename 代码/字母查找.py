def f(m,n):
    count=0
    for i in m:
        if (i in n):
            count+=1
        else:
            return ("NOT FOUND")
        if(count==len(m)):
            if(len(m)>len(n)):
                return ("NOT FOUND")
            else:
                return ("FOUND")
            #定义函数体完成题目要求功能
m=input()
n=input()
count=0
for i in m:
    if(ord('A')<=ord(i)<=ord('z')):
        count+=1
    else:
        print('ERROR')
        break
    if(ord('A')<=ord(i)<=ord('Z')):
        print("NOT FOUND")
        break
if(count==len(m)):
    print(f(m,n))


def f(m, n):
    for i in m:
        if n.count(i) > 0:
            n = n.replace(i, '', 1)
        else:
            return 'NOT FOUND'
    return 'FOUND'
m = input()
if m.isalpha():
    n = input()
    print(f(m, n))
else:
    print('ERROR')

