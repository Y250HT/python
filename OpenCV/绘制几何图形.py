import cv2
import numpy as np

'''
图像合成
	能够在图像上绘制几何形状；
	能够实现图像叠加；
	能够在图像上指定位置显示文字；
①	问题描述
在图像上指定位置添加指定直线、矩形、圆、多边形等几何形状，并在指定位置写一段文字。
②	解题思路
读取图像后，通过OpenCV的line/rectangle/circle/polylines等方法可以绘制直线/矩形/圆形/多边形等几何形状，
这些方法的参数可以指定位置、粗细、颜色。通过putText方法可以在图像上写文字，可用来对图像做标注。
'''

##############################图像合成##################################
def draw_image():
    path = 'yaz.jfif'
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # 在图的上方画5条平行线
    for i in range(5):
        # 几个参数含义： 要在其上绘制直线的图像， 直线起点坐标， 直线终点坐标， 颜色（rgb)，线条宽度
        cv2.line(img, (20, 20+i*20), (520, 20+i*20), (0, 0, 50*(i+1)), 3)
    # 绘制一个黄色大矩形
    # 参数含义： 图像， 左上角顶点坐标，右下角顶点坐标，颜色bgr， 线条宽度
    cv2.rectangle(img, (10, 10), (600, 400), (0, 255, 255), 6)
    # 画一个圆
    # 参数含义： 图像， 圆心坐标， 半径， 颜色bgr, 线条宽度
    cv2.circle(img, (300, 200), 180, (0, 255, 0), 3)
    # 绘制多边形(五边形)
    pts = np.array([[30, 150], [150, 350], [400, 330], [500, 250], [350, 100]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(img, [pts], True, (200, 0, 0), 3)
    # 选择字体
    font = cv2.QT_FONT_NORMAL
    # 参数含义： 图像，要显示的文字，坐标，字体，字号，颜色，粗细
    cv2.putText(img, 'hello openCV', (100, 300), font, 2, (0, 0, 0), 4)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    draw_image()        #####图像合成
