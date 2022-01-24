sum=1
def jiec(n):
    global sum
    if(n==3):
        return 3
    else:
        return n*jiec(n-1)
print(jiec(20))