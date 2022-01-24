def huiwen(n):
    if(n[::-1]==n):
        print("%s是回文数" % n)
    else:
        print("%s不是回文数" % n)
while(1):
    huiwen(input())