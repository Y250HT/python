import cv2
import warnings
# warnings Python 中红色警告部分太多时可选择用代码忽略这些警告
import matplotlib.cbook
import matplotlib.pyplot as plt

img = cv2.imread('PIC.jfif')
# 转换BGR为RGB
img = img[:, :, (2, 1, 0)]
# 边界填充常用到cv2.copyMakeBorder(),它也包括多种方法
# BORDER_DEFAULT 将最近的像素复制填充
# BORDER_REPLICATE 复制最近的一行或一列像素并一直延伸至添加边缘
# BORDER_REFLECT 反射法，对感兴趣的图像中的像素在两边进行复制
# BORDER_REFLECT_101 反射发，也就是以最边缘像素为轴，对称复制
# BORDER_WRAP 外包装法，相当于截断复制
# BORDER_CONSTANT 常量法，常量值填充

# 选择上下左右扩充的长度，这里选择的均为30
reflect = cv2.copyMakeBorder(img, 30, 30, 30, 30, borderType=cv2.BORDER_REFLECT)
default = cv2.copyMakeBorder(img, 30, 30, 30, 30, borderType=cv2.BORDER_DEFAULT)
replicate = cv2.copyMakeBorder(img, 30, 30, 30, 30, borderType=cv2.BORDER_REPLICATE)
reflect101 = cv2.copyMakeBorder(img, 30, 30, 30, 30, borderType=cv2.BORDER_REFLECT_101)

# plt.subplot(2,3,1)也可以写成plt.subplot(231)，表示把显示界面分割成2*3的网格，其中第一个参数是行数，第二个是列数，第三个是表示图形的标号
plt.subplot(231), plt.imshow(img), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(reflect), plt.title('REFLECT')
plt.subplot(233), plt.imshow(default), plt.title('DEFAULT')
plt.subplot(234), plt.imshow(replicate), plt.title('REPLICATE')
plt.subplot(235), plt.imshow(reflect101), plt.title('REFLECT101')
plt.savefig('padding.png')

#  图像的融合操作
cat = cv2.imread('yaz.jfif')
dog = cv2.imread('zcr.webp')
# 先重新设置尺寸
cat_resize = cv2.resize(cat, (550, 366))
dog_resize = cv2.resize(dog, (550, 366))
# 图像融合的操作使用cv2.addWeighted(),最后为gamma值，可以理解为图像的偏移量
res = cv2.addWeighted(cat_resize, 0.7, dog_resize, 0.3, 0)
cv2.imwrite('dd.png',res)
