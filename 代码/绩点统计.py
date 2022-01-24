dic={'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,\
     'C-':1.5,'D':1.3,'D-':1.0,'F':0}
sum=0
c=0
while True:
    a=input()
    if a == '-1':
        break
    else:
        b=int(input())
    sum=sum+dic[a]*b
    c=c+b
print('%.2f'%(sum/c))