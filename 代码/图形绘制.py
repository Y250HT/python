import turtle
# 三角形
turtle.pensize(3)
# 抬起画笔
turtle.penup()
# 移动到指定位置
turtle.goto(-200, -50)
# 放下画笔
turtle.pendown()
# 开始填充
turtle.begin_fill()
# 填充颜色
turtle.color('red')
# 半径为40
turtle.circle(40, steps=3)
# 填充结束
turtle.end_fill()
# 正方形
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(40, steps=4)
turtle.end_fill()
# 五边形
turtle.penup()
turtle.goto((0, -50))
turtle.pendown()
#
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(40, steps=5)
turtle.end_fill()
# 六边形
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('seashell')
turtle.circle(40, steps=6)
turtle.end_fill()
# 圆形
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.begin_fill()
turtle.color('purple')
turtle.circle(40)
turtle.end_fill()
# 文字
turtle.color('green')
turtle.penup()
turtle.goto(-100, 50)
turtle.pendown()
turtle.write("Cool Colorful Shapes", font=("Times", 18, "bold"))
# 可见性，隐藏海龟，也就是海龟画笔
turtle.hideturtle()
turtle.done()
