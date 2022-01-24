n = int(input())
if 1<=n<=46 or n==48 or 50<=n<=52 or n==54:
    for i in range(10000, 1000000):
        num = str(i)
        if num == num[::-1]:
            if n == sum(int(j) for j in num):
                print(num)
elif n==47 or n==49 or n==53:
    print("无满足条件的数！")
else:
    print("输入错误，请重新输入！")