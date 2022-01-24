string = "他问,你知道cba是什么单词的缩写么    ?    "
print(string)
print('1.删除空格')
print('2.英文标点替换')
print('3.首字母大写')
print('4.退出')

while True:
    option = input("请输入功能选项：\n")
    if option=='1':
        string = string.replace(' ','')
        print(string)
    elif option =='2':
        # 替换英文标点
        for i in string:
            if i == ',':
                string = string.replace(',', '，')
            elif i == '.':
                string = string.replace('.', '。')
            elif i == '?':
                string = string.replace('?', '？')
            elif i == '?':
                string = string.replace("' ", "’")
        string =string
        print(string)
    elif option =='3':
        # 首字母大写
        string = string.upper()
        print(string)
    elif option == '4':
        break