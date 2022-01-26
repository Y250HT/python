import cv2
import matplotlib.pyplot as plt

img_f = cv2.imread('ccc.png')
img = cv2.cvtColor(img_f, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img_f, cv2.COLOR_RGB2GRAY)
# cv2.threshold()可以进行阈值分割处理,其中thresh为返回图像，他也包括多种类型
# cv2.THRESH_BINARY 超过阈值部分取最大值，否则取0
# cv2.THRESH_BINARY_INV 超过阈值取0，否则取最大值
# cv2.THRESH_TRUNC 大于阈值部分设为阈值，否则不变
# cv2.THRESH_TOZERO 大于阈值部分不改变，否则设为0
# cv2.THRESH_TOZERO_INV 大于阈值部分为0，否则不变

# 不使用gray转换过的图像也可以，就是彩色的,阈值为150， 最大值为255
ret1, thresh1 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
ret3, thresh3 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TRUNC)
ret4, thresh4 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO)
ret5, thresh5 = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO_INV)

# 作图并保存到指定路径
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    # plt.imshow(),第二个是name，按规矩给就行，不需要特别关注
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    # 设置x或y轴对应显示的标签
    plt.xticks([]),plt.yticks([])
plt.savefig('finally.png')
