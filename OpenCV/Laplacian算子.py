# Laplacian算子具有单独的计算函数，即cv2.Laplacian(src,数据转换，ksize核)
# 处理后的图像会处理掉毛刺，边缘更清晰Laplacian 算子对噪声比较敏感
# 由于其算法可能会出现双像素边界，常用来判断边缘像素位于图像的明区或暗区，很少用于边缘检测
import cv2

img = cv2.imread('mountain.png')
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 高斯滤波处理图像
grayImage = cv2.GaussianBlur(grayImage, (5, 5), 0, 0)
# 拉普拉斯算法,dst就是返回的结果图像
dst = cv2.Laplacian(grayImage, cv2.CV_16S, ksize=3)
# 数据格式转换
Laplacoan = cv2.convertScaleAbs(dst)
cv2.imwrite('laplacian.png', Laplacoan)