from turtle import *
from datetime import *

def skip(step):
    '''
    跳跃给定的距离
    '''
    penup()
    forward(step)
    pendown()


def setup_clock(radius):
    '''
    建立钟表的外框
    '''
    reset()
    pensize(7)   	 	# 设置画笔线条的粗细
    for i in range(60):
        skip(radius)  	# 在距离圆心为r的位置落笔
        if i % 5 == 0:  # 若能整除5，则画一条短直线
            forward(20)
            skip(- radius - 20)
        else:          	# 否则画点
            dot(5)
            skip(-radius)
        right(6)


def make_hand(name, length):
    '''
    注册turtle形状，建立名字为name的形状
    '''
    reset()
    skip(-0.1 * length)
    # 开始记录多边形的顶点
    begin_poly()
    forward(1.1 * length)
    # 停止记录多边形的顶点,并与第一个顶点相连
    end_poly()
    # 返回最后记录的多边形
    handForm=get_poly()
    # 注册形状，命名为name
    register_shape(name, handForm)


def init():
    global secHand, minHand, hurHand, printer
    # 重置turtle指针向北
    mode("logo")
    # 建立3个表示表针的Turtle对象并初始化
    secHand = Turtle()
    make_hand("secHand", 130)   # 秒针
    secHand.shape("secHand")
    minHand = Turtle()
    make_hand("minHand", 125)   # 分针
    minHand.shape("minHand")
    hurHand = Turtle()
    make_hand("hurHand", 90)    # 时针
    hurHand.shape("hurHand")
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)     # 调整3根指针的粗细
        hand.speed(0)             	# 设置移动速度
    # 建立并输出文字的Turtle对象
    printer = Turtle()
    printer.hideturtle()
    printer.penup()


def week(t):
    week=["星期一","星期二","星期三","星期四","星期五","星期六","星期七"]
    return week[t.weekday()]


def day(t):
    return "%s %d %d" %(t.year,t.month,t.day)


def tick():
    '''
    绘制钟表的动态显示
    '''
    t = datetime.today()           # 获取本地当前的日期与时间
    # 处理时间的秒数、分钟数、小时数
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + t.second / 60.0
    hour = t.hour + t.minute / 60.0
    # 将secHand 、minHand 和hurHand 的方向设为指定的角度
    secHand.setheading(second * 6)
    minHand.setheading(minute * 6)
    hurHand.setheading(hour * 30)
    tracer(False)
    printer.fd(70)                  # 向前移动指定的距离
    # 根据 align（对齐方式）和font（字体)，在当前位置写入文本
    printer.write(week(t),align="center",font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(day(t),align="center",font=("Courier", 14, "bold"))
    # 调用 home() 方法将位置和方向恢复到初始状态, 位置的初始坐标为（0,0 ）,
    # 初始方向有两种情况：若为"standard" 模式，则初始方向为right ，表示朝向东；
    # 若为 "logo" 模式，则初始方向是up，表示朝向北
    printer.home()
    tracer(True)
    # 设置计时器，100ms 后继续调用 tick() 函数
    ontimer(tick,100)


def main():
    # 关闭绘画追踪，可以用于加速绘画复杂图形
    tracer(False)
    init()
    # 画表框
    setup_clock(200)
    # 开启动画
    tracer(True)
    tick()
	# 启动事件循环,开始接收鼠标的和键盘的操作
    done()


main()