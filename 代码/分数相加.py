def js(a):
    i=1
    sum=0
    while(i<=a):
        sum+=1/i
        i+=2
    print("%.2f" %  sum)

def os(a):
    i=2
    sum=0
    while(i<=a):
        sum+=1/i
        i+=2
    print("%.2f" %  sum)

n=eval(input())
if(n%2==0):
    os(n)
else:
    js(n)