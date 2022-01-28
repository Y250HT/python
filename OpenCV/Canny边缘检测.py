# Canny 边缘检测算子是一种多级检测算法
# 检测算法应该精确地找到图像中的尽可能多的边缘，尽可能的减少漏检和误检
# 最优定位：检测的边缘点应该精确地定位于边缘的中心
# 图像中的任意边缘应该只被标记一次，同时图像噪声不应产生伪边缘
# 需要使用Canny（x导数，y导数，低阈值，高阈值）函数即可
import cv2

img = cv2.imread('mountain.png')
# 高斯滤波边缘检测
blur = cv2.GaussianBlur(img, (3, 3), 0)
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# 重要点，求xy方向的Sobel算子
gradx = cv2.Sobel(blur, cv2.CV_16SC1, 1, 0)
grady = cv2.Sobel(blur, cv2.CV_16SC1, 0, 1)
# 使用canny函数处理图像，x，y分别是上一步求出来的梯度，低阈值50，高阈值150
edge_output = cv2.Canny(gradx, grady, 50, 150)
cv2.imwrite('canny.png', edge_output)