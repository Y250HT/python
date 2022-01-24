# 猜年龄
# 美国数学家维纳(N.Wiener)智力早熟，11 岁就上了大学。他曾在 1935~1936 年应邀
# 来中国清华大学讲学。一次，他参加某个重要会议，年轻的脸孔引人注目。于是有
# 人询问他的年龄，他回答说：“我年龄的立方是个 4 位数。我年龄的 4 次方是个 6
# 位数。这 10 个数字正好包含了从 0 到 9 这 10 个数字，每个都恰好出现 1 次。” 请
# 编程输出当年维纳的年龄
for age in range(1,200):
    three=str(age**3)
    if len(three)!=4:
        continue
    four=str(age**4)
    if len(four)!=6:
        continue
    s=three+four
    if len(set(s))==10:
        print(age)
        break
