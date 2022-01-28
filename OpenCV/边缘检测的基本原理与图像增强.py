# 边缘检测的流程的基本步骤为图像滤波，边缘增强，边缘检测

import cv2
import numpy as np
# 1.灰度模式读取图像
# 2.numpy对梯度进行数值计算，所以要使用CHR.astype('float')进行格式变换
# 接下来均是固定操作
CHR = cv2.imread('train.png', 0)
CHR= CHR.astype('float')
row, column = CHR.shape
gradient = np.zeros((row, column))
for x in range(row-1):
    for y in range(column-1):
        gx = abs(CHR[x+1, y] - CHR[x, y])
        gy = abs(CHR[x, y+1] - CHR[x, y])
        gradient[x, y] = gx +gy
# 3.对图像进行增强，增强后的图像命名为sharp
sharp = CHR + gradient
sharp = np.where(sharp > 255, 255, sharp)
sharp = np.where(sharp < 0, 0, sharp)
# 数据类型变换
gradient = gradient.astype('uint8')
sharp = sharp.astype('uint8')
# 保存图像
cv2.imwrite('train1.png', gradient)
