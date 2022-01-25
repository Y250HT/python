import cv2
import numpy as np

def contour_area():
    img0 = cv2.imread('yaz.jfif')
    # cv2.imshow('original', img0)
    img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 复制原图
    img1 = img0.copy()
    # 创建一幅相同大小的白色图像
    img2 = np.ones(img.shape)
    # 按照面积将所有轮廓逆序排序
    contours2 = sorted(contours, key=lambda a: cv2.contourArea(a), reverse=True)
    i = 0
    for c in contours2:
        area = cv2.contourArea(c)
        print(area)
        i+=1
        if i>=10:break
        # 分别在复制的图像上和白色图像上绘制当前轮廓
        cv2.drawContours(img1, [c], 0, (200, 0, 128), 3)
        cv2.drawContours(img2, [c], 0, (0, 0, 128), 3)
    # plot_images(1,3,[img,img1,img2])
    cv2.imshow('con1', img1)
    cv2.imshow('con2', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


contour_area()