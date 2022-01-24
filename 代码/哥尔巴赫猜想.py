# 哥德巴赫猜想
# 数学领域著名的“哥德巴赫猜想”的大致意思是：任何一个大于 2 的偶数总能表示
# 为两个素数之和。例如：24=5+19，其中 5 和 19 都是素数。本实验的任务是设计一
# 个程序，验证 20 亿以内的偶数都可以分解成两个素数之和。输入一个大于 2 的正整
# 数，当输入为偶数时，在一行中按照格式“N = p + q”输出 N 的素数分解，其中
# p 、 q 均为素数且 p ≤ q。因为这样的分解可能不唯一（例如 24 还可以分解
# 为7+17），要求必须输出所有解中 p最小的解。当输入为奇数时，输出'Data error!' 。

#程序1
def isPrime(n):          #判断素数的函数
    if n < 2:
        return False     #0和1不是素数
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True
N = int(input())        #接收用户输入并转成整数
if N % 2 == 0:  #判断输入的数为偶数
    for i in range(N):
        if isPrime(i) and isPrime(N - i) : #判断分解的两个均为素数,如果满足则进行输出
            print("{} = {} + {}".format(N, i,N-i))
            break
else:
    print('Data error!')


#程序2在判断素数的过程中进行了程序优化
#程序2
# def isPrime(n):  # 定义判断素数的函数
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return 0
#     return 1
#
# def image(n):
#     for i in range(2,int(n ** 0.5) + 1):
#         if isPrime(i) == 1 and isPrime(n-i) == 1:
#             p = i
#             q = n - i
#             print("N = %d + %d" % (p,q))
#
# n = int(input())
# if n % 2 == 0:
#     #执行所定义的函数
#     image(n)
# else:
#     print("Data error!")