# 采用的是张正友的相机标定
# 使用函数cv2.findChessboardCorners()函数寻找角点
# 使用函数cv2.cornerSubPix(),返回检查出的亚像素级角点
# 世界坐标系：用户定义的三维世界坐标系，为了描述目标物在真实世界里的位置而被引入，单位为m
# 相机坐标系：在相机上建立的坐标系，为了从相机的角度描述物体位置而定义，作为沟通世界坐标系和图像/像素坐标系的中间一环，单位为m
# 图像坐标系：为了描述成像过程中，物体从相机坐标系到图像坐标系的投影投射关系而引入，方便进一步得到像素坐标系下的左边，单位为m
# 像素左边系：为了描述物体丞相后的像点在数字图像上（相片）的坐标而引入，是我们真正从相机内读取的信息所在坐标系，单位为个（像素数目）
# 需要使用cv2.FindChessboardCorners(image,patternSize,corners,flags,retvalgray,corners) 函数
# patternsize是棋盘的尺寸，corners存放角点的位置，flags迭代的准则，retvalgray是否检测出角点，corners角点的位置
# 然后需要使用corners = cv2.cornerSubPix(image, corners, winSize, zeroZone, criteria）执行亚像素角点检测
# corners初始角点坐标向量，同时作为亚像素坐标位置的输出，所以需要是浮点型的数据，WinSize大小为搜索窗口的一般
# zeroZone死区的一半尺寸，死区是不对搜索区的中央位置做求和运算的区域，（-1，-1）表示没有死区
# criteria定义求角点的迭代过程的终止条件，可以为迭代次数和角点精度两者的组合
import cv2
import numpy as np


# criteria:角点精准化迭代过程的终止条件（迭代30次或移动0.001）
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((7*7, 3), np.float32)

# 设定世界坐标下的坐标值，因为用的是棋盘可以直接按网格取
# 假定棋盘正好在x-y平面上，这样z值直接取0，简化初始化步骤
# mgrid把列向量[0:cbrow]复制了cbcol列，把行向量[0:cbcol]复制了cbrow行
# 转置reshape之后，每行都是4*6网格中的某个点的坐标
objp[:,:2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)
objpoints = []
imgpoints = []
img = cv2.imread('image.png')
cv2.imwrite('test1.png', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 寻找角点，存入corners，ret是找到角点的flag
ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)

# 执行亚像素角点检测
if ret == True:
    objpoints.append(objp)
    #------begin
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    #------end
    imgpoints.append(corners2)
    # 在棋盘上绘制角点
    img = cv2.drawChessboardCorners(img, (7, 7), corners2, ret)
    cv2.imwrite('img.png', img)