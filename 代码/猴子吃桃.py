#猴子吃桃
# 请用函数编程实现。
# 猴子第一天摘下若干个桃子，立即吃了一半，还不过瘾又多吃了一个，第二天将第一天
# 剩下的桃子吃了一半又多吃了一个，以后每天以这个规律吃下去，到第十天再去吃时发
# 现只剩下一个桃子，问猴子第一天摘了多少个桃子？

def f(n):
    if n==10:
        return 1
    else:
        return (f(n + 1) + 1) * 2;
print(f(1))