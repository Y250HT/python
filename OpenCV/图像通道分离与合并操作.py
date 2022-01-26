import cv2

img = cv2.imread('PIC.jfif')
# 分离图像的BGR通道
b, g, r = cv2.split(img)
cv2.imwrite('r.png', r)
cv2.imwrite('g.png', g)
cv2.imwrite('b.png', b)
# 合并BGR通道的图像
img1 = cv2.merge((b,g,r))
cv2.imwrite('re.png',img1)