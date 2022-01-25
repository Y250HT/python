import numpy as np
import cv2
import matplotlib.pyplot as plt
# 显示图像的直方图，根据的是图像的像素，灰度等
# img = cv2.imread('moon.webp', 0)
# plt.hist(img.ravel(), 255, [0, 256])
# plt.title("moon")
# plt.show()

# 直方图均衡化,可以增强图片的细节以及明暗对比
img = cv2.imread('moon.webp', 0)
plt.hist(img.ravel(), 255, [0, 256])
# 均衡化最主要的操作是equalizeHist()
moon2 = cv2.equalizeHist(img)
plt.hist(moon2.reshape(-1),bins = 256)
plt.show()
cv2.imshow('moon2', moon2)
cv2.waitKey(0)
cv2.destroyAllWindows()


