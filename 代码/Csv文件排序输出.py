# def csv_to_lst(filename):
# 	"""接收文件名为参数，读取数据到二维列表中，返回二维列表。形如
# 	[['20170101', '章阳', 'Male', 'A'],... ['20170108', '刘忆宁', 'Male', 'E']]
# 	"""
# 	with open(filename, 'r', encoding='UTF-8') as f:
# 		grade_in_lst = [line.strip().split(',') for line in f]  # 逐行切分为列表，得到二维列表
# 	return grade_in_lst
#
#
# def sort_lst(list_name, n):
# 	"""接收需要排序的二维列表名和整数的排序列序号（范围为：1，2，3，4）为参数，返回排序后的二维列表。"""
# 	list_name.sort(key=lambda x: x[n - 1])  # 列序号从1开始，列表中的序列从0开始，排序依据用x[n - 1]
# 	return list_name                        # 返回排序后的列表
#
#
# def output(ls):
# 	"""接收排序后的二维列表为参数，逐行输出，每行的元素间用制表符分隔。"""
# 	for line in ls:             # line 为子列表
# 		print(*line, sep='\t')  # *对子列表进行解包，得到多个元素，sep指定分隔符
#
#
# if __name__ == '__main__':
# 	file = 'grade0.csv'
# 	num = int(input())
# 	grade_list = csv_to_lst(file)
# 	ls_in_sort = sort_lst(grade_list, num)
# 	output(ls_in_sort)



#程序2
with open('grade0.csv', 'r', encoding='utf-8') as f:
    lines = []
    for line in f:
        line = line.replace('\n','')
        lines.append(line.split(','))
    f.close()
a = eval(input())
ls = sorted(lines,key=lambda x:x[a-1])
#利用匿名函数
for i in ls:
    print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}')
