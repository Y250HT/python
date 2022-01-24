#  汽车迷
# 小明是一个汽车迷，看到什么汽车马上就可以说出汽车的生产年份、型号和品牌。
# 定义一个函数，可以输出汽车的介绍。
# 例如输入：
# 2020 AMG_S65 奔驰
# 可以输出：
# 这是一辆 2020 年生产，型号是 AMG_S65 的奔驰牌汽车
# 要求函数具有以下功能：当用户只输入生产年份、型号时，品牌按“宝马”输出。
# 输入
# 输入用空格分隔的年、型号和品牌（品牌可能没有）
# 输出
# 这是一辆****年生产，型号是****的****牌汽车（**** 根据用户输入进行替换）


def car(year,model,brand = '宝马'):
	return f'这是一辆{year}年生产，型号是{model}的{brand}牌汽车。'
    #f-string格式化字符串输出
ls = input().split()  #以空格进行分割
print(car(*ls))
#列表前面加*号表示将列表解开成两个独立地参数，传入函数
#参数的解包 两个*是将字典解开成独立的元素作为形参