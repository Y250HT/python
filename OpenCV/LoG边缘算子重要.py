# 使用LoG算子进行边缘提取
import cv2
import numpy as np
img = cv2.imread('mountain.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 边缘扩充处理图像并使用高斯滤波处理该图像
image = cv2.copyMakeBorder(img, 2, 2, 2, 2, borderType=cv2.BORDER_REPLICATE)
img = cv2.GaussianBlur(image, (3, 3), 0, 0)
# 使用numpy定义LoG算子
m1 = np.array(
    [[0, 0, -1, 0, 0], [0, -1, -2, -1, 0], [-1, -2, 16, -2, -1], [0, -1, -2, -1, 0], [0, 0, -1, 0, 0]]
)
# 卷积操作
# 为了使卷积对每个像素都进行运算，原图像的像素边缘像素要对准模板的中心
# 由于图像边缘扩大了2像素，因此要从位置2到行（列）-1
rows = image.shape[0]
cols = image.shape[1]
image1 = np.zeros(img.shape)
for k in range(0, 2):
    for i in range(2, rows - 2):
        for j in range(2, cols - 2):
            image1[i, j] = np.sum((m1 * image[i-2:i+3, j-2:j+3, k]))

# 数据格式转换
image1 = cv2.convertScaleAbs(image1)
cv2.imwrite('log.png', image1)