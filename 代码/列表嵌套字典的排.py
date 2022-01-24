n=int(input())
a=[]
for i in range(n):
    s=input().split()
    dic=dict(name=s[0],age=int(s[1]))
    a.append(dic)
a.sort(key= lambda x: x['age'])
print(a)
a.sort(key= lambda x: x['name'])
print(a)