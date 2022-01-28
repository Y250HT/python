# 图像的腐蚀需要调用erode（）函数，而图像腐蚀的核心就是定义结构元素，即卷积核
# 可以使用自带的getStructuringElement（shape, ksize, anchor）函数，anchor: 锚点的位置。该值有默认值Point（-1,-1），表示锚点位于中心点。
# shape: 表示内核的形状。有矩形MORPH_RECT、十字形MORPH_CORSS 和椭圆形MORPH_ELLIPSE三个值选择
import cv2
img = cv2.imread('two.png')
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel1 = cv2.getStructuringElement(cv2.MARKER_CROSS, (3, 3))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
erosion1 = cv2.erode(img, kernel1)
erosion2 = cv2.erode(img, kernel2)
erosion3 = cv2.erode(img, kernel3)
cv2.imwrite('eros1.png', erosion1)
cv2.imwrite('eros2.png', erosion2)
cv2.imwrite('eros3.png', erosion3)