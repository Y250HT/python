# Roberts 算子是利用局部差分寻找边缘的一种算子，是最简单的边缘检测算子
# 检测垂直边缘的效果要优于其他方向边缘，定位精度高，但对噪声的抑制能力较弱
# 需要使用固定的np.array(),以及卷积操作，数据格式转换
# Roberts 算子对陡峭的低噪声图像效果较好，尤其是边缘正负45度较多的图像，但定位准确率较差

import cv2
import numpy as np

img = cv2.imread('road.png')
# 1.灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2.Roberts算子(固定操作)
kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
kernely = np.array([[0, -1], [1, 0]], dtype=int)
# 3.卷积操作
# 因为Roberts卷积模板含有负值，因此在filter2D（）操作后会有负值，还会有大于255的值，而原图像是uint8
# 即8位无符号数，因此要使用16位有符号的书数据类型，即cv2.CV_16S
x = cv2.filter2D(grayImage, cv2.CV_16S, kernelx)
y = cv2.filter2D(grayImage, cv2.CV_16S, kernely)
# 4.数据格式转换
# 经过处理后最后要使用convertScaleAbs（）函数将其转回原来的uint8形式，否则无法显示图像
# absX，absY返回的是两个不同方向的边缘检测图
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)
# 最后将两个图综合起来
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
cv2.imwrite('robert.png', Roberts)