count=1
def f(n):
    global count
    if(n<10):
        count=(count+1)*2
        n+=1
        return f(n)
    else:
        return count
print(f(1))