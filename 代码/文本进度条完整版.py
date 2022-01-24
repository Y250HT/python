import time
i=1
scale=50
print("执行开始".center(scale//2, "-"))
start=time.perf_counter()
#while(i!=51):
while(i!=51):
    m=i
    a='*'* m
    b='.'*(scale-m)
    c=(m/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.05)
    i+=1
print("\n"+"执行结束".center(scale//2,'-'))