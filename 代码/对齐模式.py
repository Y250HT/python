m = input("请输入对齐模式：")
s = "PYTHON"
if  m =="右":
    print("{0:*>30}".format(s))
elif  m =="中":
    print("{0:*^30}".format(s))
else:
    print("{0:*<30}".format(s))