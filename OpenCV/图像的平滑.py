import cv2
import matplotlib.pyplot as plt

img = cv2.imread('apple.png')

# 需要先转换格式，将BGR变成RGB,
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 进行图像的平滑操作需要使用各种滤波,需要指定核
# cv2.blur(image, ksize)均值滤波会使图像状况变好，但同时也使图像变的明显模糊，易收到干扰，只能相对减弱噪声
# cv2.boxFilter(src, depth(通常用-1表示与原始图像一致), ksize, normalize)方框滤波，使用的比均值滤波高，但仍然一般，有一个normalize，False则不进行均值化处理
# cv2.GuassianBlur(img, ksize, sigmaX, sigmaY)高斯滤波，需要指定sigmaX，sigmaY，为0则自己计算
# cv2.medianBlur(src, ksize)均值滤波，对消除椒盐噪声特别有用

res1 = cv2.blur(img, (5, 5))
res2 = cv2.GaussianBlur(img, (5, 5), 0, 0)
res3 = cv2.boxFilter(img, -1, (5, 5), False)
res4 = cv2.medianBlur(img, 5)

# 保存图像
titles = ['Blur', 'GaussianBlur', 'boxFilter', 'medianBlur']
images = [res1, res2, res3, res4]
for i in range(4):
    plt.subplot(2, 2, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.savefig('applefin.png')
# cv2.imshow('apple', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()