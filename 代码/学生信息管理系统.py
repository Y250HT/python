student={'202001020001':'袁红太','202001020002':'袁红太','202001020003':'袁红太','202001020004':'袁红太'}
def add(n,m):
    student[n]=m
    print(student)

def delete(n):
    student.pop(n)
    print(student)

def change(n):
    xingming = input("请输入要修改的学生的姓名\n")
    student[n]=xingming
    print(student)

while(1):
    print('='*40)
    print("学生管理系统 V21.10")
    print("1.添加学生信息\n2.删除学生信息\n3.修改学生信息\n4.查询所有学生信息\n0.退出系统")
    print('='*40)
    x=input("请输入您所需要的功能序号：")
    if(x=='1'):
        xuehao=input("请输入要添加的学生学号\n")
        xingming=input("请输入要添加的学生姓名\n")
        add(xuehao,xingming)
    elif(x=='2'):
        xuehao = input("请输入要删除的学生学号\n")
        delete(xuehao)
    elif(x=='3'):
        xuehao = input("请输入要修改的学生的学号\n")
        change(xuehao)
    elif(x=='4'):
        print(student)
    elif(x=='0'):
        break
    else:
        print("您的输入不合法，请重新输入")