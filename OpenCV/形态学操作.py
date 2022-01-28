# 图像的形态学操作包括开运算和闭运算
# 开运算可以使图像的轮廓变得光滑，还能使狭窄的连接断开和消除细毛刺
# 闭运算同样可以使图像变得光滑，并且可以天平图像中的澳西安，弥合小裂缝
# 开运算，闭运算通常使用函数moephologyEx(src， op， kernel)，且首先先进行二制化
# kernel是内核，一般要配合getStructuringElement（）使用

import cv2
img = cv2.imread('two.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二制化
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel1 = cv2.getStructuringElement(cv2.MARKER_CROSS, (10,10))
img_op = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel1)
img_cl = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel1)

cv2.imwrite('op.png', img_op)
cv2.imwrite('cl.png', img_cl)