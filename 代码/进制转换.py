num = int(input("请输入要转换的数据:\n"))
change = input("请选择转换进制：二 、八、十、十六\n")
if change == '2':
    print(f"进制转换后的数据为：{bin(num)}")
elif change == '8':
    print("进制转换后的数据为：%s" % (oct(num)))
elif change == '10':
    print("进制转换后的数据为：%d" % (int(num)))
elif change == '16':
    print("进制转换后的数据为：{}".format(hex(num)))
