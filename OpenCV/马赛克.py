import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread('wbq.webp')

    # 方法1
    # print(img.shape)高度宽度通道
    # 先缩小在放大会变得像马赛克
    # img2 = cv2.resize(img,(45,60))
    # img3 = cv2.resize(img2,(450,600))
    # cv2.imshow('bao', img3)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 方法2
    # img2 = cv2.resize(img, (45, 60))
    # # axis让轴等于0
    # # 两次repeat的意思是让他在0，1轴都拉伸重复
    # img3 = np.repeat(img2, 10, axis=0)
    # img4 = np.repeat(img3, 10, axis=1)
    # cv2.imshow('bao', img4)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # 方法3
    img2 = img[::10, ::10] # 两个轴都每隔10个像素取出一个像素直接显示的话会很小
    cv2.namedWindow('bao', flags=cv2.WINDOW_NORMAL)  # 一般的窗口
    # 调整窗口尺寸
    cv2.resizeWindow('bao', (450, 600))
    cv2.imshow('bao',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



