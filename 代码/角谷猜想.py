def guess(number):
    i = 0  # 统计变换的次数
    original_number = number  # 记录最初的number
    while number != 1:
        if number % 2 == 0:  # number为偶数
            number = number / 2
        else:  # number为奇数
            number = number * 3 + 1
        i += 1
    print(f"{original_number}经过{i}次变换后回到1")


num = int(input("请输入一个大于1的正整数:"))
guess(num)
