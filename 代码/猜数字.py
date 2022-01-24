guess_num = input("请设定要猜的数字：\n")
for frequency in range(1,6):
    number = input("请输入第"+str(frequency)+"次猜测的数字:")
    if number.isdigit() is False:
        print('请输入一个正确的数字')
    elif int(number) < 0 or int(number) > 100:
        print("请输入1-100范围的数字")
    elif int(guess_num) == int(number):
        print("恭喜你用了%d次猜对了" % frequency)
        break
    elif int(guess_num) > int(number):
        print("很遗憾，你猜小了")
    else:
        print("很遗憾，你猜大了")
    if frequency == 5:
        print("很遗憾，%d次机会已用尽，游戏结束,答案为%d" %
              (frequency, int(guess_num)))