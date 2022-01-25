import cv2
import numpy as np
if __name__ == '__main__':
    img1 = cv2.imread('PIC.jfif')
    img2 = cv2.cvtColor(img1, code = cv2.COLOR_BGR2HSV)
    #定义在HSV颜色空间中蓝色的范围
    lower_blue = np.array([100,50,50])
    upper_blue = np.array([130,255,255])
    # 根据蓝色的范围，标记图片中哪些位置是蓝色
    # inRange是否在这个范围内的蓝色
    mask = cv2.inRange(img2, lower_blue, upper_blue)
    res = cv2.bitwise_and(img1, img1, mask = mask)
    # 将图片中全部由黑色变成白色
    # res.shape[0]代表高度[1]代表宽度
    for i in range(res.shape[0]):
        for j in range(res.shape[1]):
            # .all意思是应用到三个像素，并非一维，全为0才是黑色，全为255为白色
            if(res[i,j] == 0).all():
                res[i,j] = 255
    cv2.imshow('hsv', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()