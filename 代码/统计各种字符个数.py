n=input()
a=b=c=d=e=0
for i in n:
    if(ord(i)>=ord("a") and ord(i)<=ord("z")):
        a+=1
    elif(ord(i)>=ord("A") and ord(i)<=ord("Z")):
        b+=1
    elif(i>="0" and i<="9"):
        c+=1
    elif(i == " "):
        d+=1
    else:
        e+=1
print(a,b,c,d,e)