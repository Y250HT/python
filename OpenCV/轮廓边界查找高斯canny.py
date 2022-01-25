import cv2
import numpy as np
if __name__=='__main__':
    dog = cv2.imread('yaz.jfif')
    gray = cv2.cvtColor(dog, cv2.COLOR_BGR2GRAY)
    # way1
    # 核越大，越模糊，但是只能是奇数
    gray2 = cv2.GaussianBlur(gray, (5, 5), 1)
    # 阈值越小，产生的画面细节越多
    # canny = cv2.Canny(gray2, 0, 10)
    canny = cv2.Canny(gray2, 75, 200)
    cv2.imshow('cvr', canny)

    # way2
    # 感觉用处不大
    # areas = []
    # threshold, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_OTSU)
    # contours, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # for contour in contours:
    #     areas.append(cv2.contourArea(contour))
    # areas = np.asarray(areas)
    # index = areas.argsort()
    # # 第二大的轮廓就是轮廓，为固定语句
    # mask = np.zeros_like(gray, dtype=np.uint8)
    # mask = cv2.drawContours(mask, contours, index[-2], (255, 255, 255), thickness=-1)
    cv2.imshow('face', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()