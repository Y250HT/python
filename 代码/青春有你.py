player_info = {}
li = []
print('输入quit表示选手成绩录入完毕')
while True:
    name = input("请输入选手名称：\n")
    if name == 'quit':
        break
    score = float(input("请输入选手票数：\n"))
    player_info[name] = score
items = player_info.items()
for j in items:
    li.append([j[1], j[0]])
# 转换为list类型，进行排序
li.sort()
# 获取选手索引
count = len(li) - 1
# 输出排名
for i in range(1, len(li) + 1):
    print(f"第{i}名：{li[count][1]},成绩为{li[count][0]}分")
    count -= 1