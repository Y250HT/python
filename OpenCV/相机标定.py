# 利用获取到的棋盘标定图的内角点图像坐标之后，就可以用calibrateCamera（）函数进行标定
# ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objectPoints,
# imagePoints, imageSize, cameraMatrix, distCoeffs[, rvecs[, tvecs[,
# flags[, criteria]]]])
# objectPoints是世界坐标系中的三维点，imgpoints为每一个内角点对应的图像坐标点，imagesize为图像的像素尺寸大小
# cameraMatrix为相机的内参矩阵，distCoeffs为畸变矩阵，rvecs为旋转向量，tvecs为位移变量，
# flags为标定时采用的算法，有
# CV_CALIB_USE_INTRINSIC_GUESS：使用该参数时，在cameraMatrix矩阵中应该有fx,fy,u0,v0的估计值。否则的话，将初始化(u0,v0）图像的中心点，使用最小二乘估算出fx，fy。
# CV_CALIB_FIX_PRINCIPAL_POINT：在进行优化时会固定光轴点。当CV_CALIB_USE_INTRINSIC_GUESS参数被设置，光轴点将保持在中心或者某个输入的值。
# CV_CALIB_FIX_ASPECT_RATIO：固定fx/fy的比值，只将fy作为可变量，进行优化计算。当CV_CALIB_USE_INTRINSIC_GUESS没有被设置，fx 和 fy 将会被忽略。只有fx/fy的比值在计算中会被用到。
# CV_CALIB_ZERO_TANGENT_DIST：设定切向畸变参数（p1,p2）为零。
# CV_CALIB_FIX_K1,…,CV_CALIB_FIX_K6：对应的径向畸变在优化中保持不变。
# CV_CALIB_RATIONAL_MODEL：计算k4，k5，k6三个畸变参数。如果没有设置，则只计算其它 5 个畸变参数。
# 其中ret：教程成功与否，布尔类型变量，mtx相机内参，dist畸变系数，revcs旋转矩阵，tvecs平移矩阵
# 对图像进行即便的矫正使用undistort（）函数实现dst = undistort(src, cameraMatrix, distCoeffs[, dst[, newCameraMatrix]])
# cameraMatrix为之前求得到的相机内参矩阵，distCoeffs为之前求得的相机畸变矩阵，dst矫正后的图像，newCameraMatrix可以指定新的相机参数

import cv2
import numpy as np
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((7*7, 3), np.float32)

objp[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)
objpoints = []
imgpoints = []
img = cv2.imread('gezi.png')
cv2.imwrite('test2.png', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 寻找角点，存入corners，ret是找到的角点的flag
ret, corners = cv2.findChessboardCorners(gray, (7, 7), None)
# 亚像素级角点检测
if ret == True:
    objpoints.append(objp)
    #---begin
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    #---end
    imgpoints.append(corners2)
    # 在棋盘上绘制角点
    img = cv2.drawChessboardCorners(img, (7, 7), corners2, ret)

# 传入所有图片各自角点的三维，二维坐标，相机标定
# 每张照片都有自己的旋转个平移矩阵，但是相机内参和畸变系数只有一组
# mtx相机内参，dist畸变系数，revcs旋转矩阵，tvecs平移矩阵
# ---BEGIN
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, criteria)# ---end
h, w = img.shape[:2]
# 优化相机内参，这一步可选，参数1表示保留所有像素点，同时可能引入黑色像素，设为0表示尽可能裁剪所有不想要的像素，这是一个scale，0-1都可选
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
# 纠正畸变
# ---begin
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# ---end
# 这一步只是输出纠正畸变以后的图片
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png', dst)