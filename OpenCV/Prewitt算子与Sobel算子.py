# 只是算子不同，其余操作均与Roberts算子相同,得出的图片要更清晰
# Sobel 算子考虑了综合因素，对噪声较多的图像处理效果更好
# 故 Prewitt 算子的边缘检测结果在水平方向和垂直方向均比 Roberts 算子更加明显。Prewitt 算子适合用来识别噪声较多、灰度渐变的图像
import cv2
import numpy as np

img = cv2.imread('road.png')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 求Sobel算子
x = cv2.Sobel(grayImage, cv2.CV_16S, 1, 0)
y = cv2.Sobel(grayImage, cv2.CV_16S, 0, 1)

# 数据格式切换
absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

# 组合图形
Sobel = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 保存图像
cv2.imwrite('sobel.png', Sobel)