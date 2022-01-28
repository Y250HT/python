# 图像的膨胀结果会使图像看起来虚化,依然需要二制化以及取核操作
# 主要使用的函数为cv2.dilate(src, kernel, iterations) iterations：表示迭代次数，默认为1。

import cv2

img = cv2.imread('two.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel1 = cv2.getStructuringElement(cv2.MARKER_CROSS, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate1 = cv2.dilate(img, kernel1, iterations=1)
dilate2 = cv2.dilate(img, kernel2, iterations=1)
dilate3 = cv2.dilate(img, kernel3, iterations=1)
cv2.imwrite('dlt1.png', dilate1)
cv2.imwrite('dlt2.png', dilate2)
cv2.imwrite('dlt3.png', dilate3)