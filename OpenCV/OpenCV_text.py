'''
图像颜色处理.平滑
	理解灰度图片的概念；
	能够将彩色图片转换成灰度图片；
	理解阈值的概念；通过在灰度图片中设置阈值，提取图片中一部分图像；
	理解颜色过滤的概念；能够进行颜色过滤；
'''

import cv2
import numpy as np



########################灰度图片############################
'''
将彩色图片转换为灰度图片并显示。
imread读取图片文件时，使用cv2.IMREAD_GRAYSCALE参数，可将图片读取为灰度模式。
注：在前面的例子中，是以cv2.IMREAD_COLOR参数读取，图片就是彩色的。
'''
def gray_image():
    # 设置图片路径
    path = 'D:/2022_Work/Code/Python/OpenCV/pic_get/dog.png'
    # 读取图片，以灰度模式
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 显示图片，窗口名为image
    cv2.imshow('image', img)
    # 待用户按钮
    cv2.waitKey(0)
    # 关闭所有窗口
    cv2.destroyAllWindows()




#######################滑块控件############################
'''
在OpenCV处理图片时，有时需要频繁尝试不同的参数值（例如颜色值）来观察图片处理效果。这种情况下，使用滑块控件Trackbar可以方便和直观的修改参数的值。
本例用3个不同的滑块控件分别表示颜色的RGB分量，通过滑块拖动改变三个分量，组成不同的颜色并显示。

用三个Trackbar分别表示R/G/B颜色分量，每个Trackbar的取值范围都是0-255，当Trackbar数值变化时，重新计算颜色值并显示。
'''
img = None
def trackbar_demo():
    global img
    # 创建一个纯黑色图片并显示
    img = np.zeros((300, 500, 3), np.uint8)
    cv2.imshow('image',img)
    # 在窗口上添加3个trackbar
    # 创建trackbar的4个参数分别是：标题文字、所在窗口名、最小值、最大值、发生变化时调用的函数名
    cv2.createTrackbar('R', 'image', 0, 255, repaint)
    cv2.createTrackbar('G', 'image', 0, 255, repaint)
    cv2.createTrackbar('B', 'image', 0, 255, repaint)
    while True:
        cv2.imshow('image', img)
        # 接受按键退出
        k = cv2.waitKey(10) & 0xFF
        if k == ord('q'):
            break
    cv2.destroyAllWindows()

def repaint(x):
    global img
    # 取得3个trackbar的当前值
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    # 以三个分量值设置图片像素
    img[:] = [b, g, r]


############################图像阈值##########################
'''
通过设置合适的阈值，突出显示图像中的某一部分。
'''
img = None
# 选择合适的阈值，突出显示车道
def threshold_line():
    global img
    # 设置图片路径
    path = 'D:/2022_Work/Code/Python/OpenCV/pic_get/dog.png'
    # 读取图片
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    # 在窗口上添加1个trackbar
    cv2.createTrackbar('threshold', 'image', 0, 255, apply_threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def apply_threshold(x):
    global img
    # 将图片转换为灰度模式
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, img2 = cv2.threshold(gray, x, 255, cv2.THRESH_BINARY)
    cv2.imshow('threshold', img2)

########################图像平滑#########################
'''
	理解卷积的概念，理解核的概念和作用；
	会用卷积进行图像平滑；
	理解常用的图像平滑方法及其代码实现；
①	问题描述
通过图像平滑可以去除图像中的毛刺，便于后续处理。OpenCV中有多种不同的方式可以实现图像平滑。
②	解题思路
读取原始图像，通过trackbar选择不同的卷积核大小，实现图像平滑。
'''
img = None
def blur_demo():
    global img
    # 设置图片路径
    path = 'D:/2022_Work/Code/Python/OpenCV/pic_get/'
    # 读取图片
    img = cv2.imread(path + 'dog.png', cv2.IMREAD_COLOR)
    # 显示图片
    cv2.imshow('image', img)
    cv2.createTrackbar('kernel', 'image', 1, 30, apply_blur)
    cv2.createTrackbar('type', 'image', 1, 3, apply_blur)
    # 待用户按钮
    cv2.waitKey(0)
    # 关闭所有窗口
    cv2.destroyAllWindows()

def apply_blur(x):
    global img
    # 取得核大小
    kernel = cv2.getTrackbarPos('kernel', 'image')
    # 取得平滑方式
    type = cv2.getTrackbarPos('type','image')
    dst = None
    if type == 1:
        # 平均值
        dst = cv2.blur(img, (kernel, kernel))
    elif type == 2:
        # 高斯过滤
        dst = cv2.GaussianBlur(img,(kernel,kernel),0)
    elif type == 3:
        # 中值过滤
        dst = cv2.medianBlur(img, kernel)
    # 显示平滑后的图片
    cv2.imshow('blur', dst)


########################################################################
if __name__ == '__main__':
    #gray_image()               #灰度图
    #trackbar_demo()            #滑块控件
    #threshold_line()           #图像阈值
    blur_demo()                #图像平滑