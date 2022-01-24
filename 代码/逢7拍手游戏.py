for i in range(1, 101):
    # 判断条件：既不包含7，也不是7的倍数
    if "7" in str(i)  or int(i) % 7 == 0:
        # 输出，去掉了换行符
        print('*', end="、")
        # 如果包含7 输出*
    elif "7" not in str(i)and int(i) % 7 != 0 :
        print(i, end='、')
