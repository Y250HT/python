# 约瑟夫环问题
# 据说著名历史学家 Josephus 有过以下的故事：Josephus 及他的朋友共 41 人围成一个圆
# 圈，由第 1 个人开始报数，每数到 3 该人就必须出去，然后再由下一个人重新报数，直
# 到圆圈上少于 3 人为止。Josephus 将朋友与自己安排在第 16 个与第 31 个位置，成为最
# 后剩下的人。
# 扩展这个问题，当人数为 n，每次报数为 k 时，求解最后的 K-1 个剩下的人的位置
# 输入格式
# 在同一行内输入两个正整数 n 和 k，要求 k > = 2 且 n >= k
# 输出格式
# 以列表形式显示剩余的人的序号（如果 k<2 或者 n<k,打印"Data Error!")


def Josephus(n,k):
    ls_n = list(range(1,n+1))  #利用列表进行报数的模拟过程
    while len(ls_n) > k-1:
        ls_n = ls_n[k:] + ls_n[:k-1]
    return ls_n

n,k = map(int,input().split())
if k >= 2 and n >= k:
    print(Josephus(n,k))
else:
    print('Data Error!')