goods=[{"name":"电脑","price":4999},
{"name":"鼠标","price":80},
{"name":"游艇","price":200000},
{"name":"别墅","price":2000000}]
all=int(input())
for n, i in enumerate(goods):
    print(n,i['name'])
num=int(input())
if goods[num]['price']<=all:
    print('恭喜你成功购买一个{}'.format(goods[num]['name']))
else:
    print('账户余额不足,先去赚钱吧！')