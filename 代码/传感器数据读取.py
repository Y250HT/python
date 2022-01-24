f = open("sensor-data.txt", "r")
avg, cnt = 0, 0
#avg——总光照 cnt —— 数量
maxv, minv = 0, 9999
#最大/最小值
for line in f:
    ls = line.split()
    cnt += 1
    val = eval(ls[4])
    avg += val
    if val > maxv:
        maxv = val
    if val <minv:
        minv = val
print("最大值、最小值、平均值分别是：{:.2f},{:.2f},{:.2f}".format(maxv, minv, avg/cnt))
f.close()
