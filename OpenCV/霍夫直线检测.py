import cv2
import numpy as np

def hough_line():
    path = 'D:/2022_Work/Code/Python/OpenCV/pic_get/qp.png'
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    # 转换为灰度图并模糊
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (5, 5))
    # canny边缘检测
    edges = cv2.Canny(gray, 20, 80)
    # 霍夫直线检测
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # 画出所有直线
    for line in lines:
        for rho, theta in line:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 128), 2)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    # 关闭所有窗口
    cv2.destroyAllWindows()

if __name__ == '__main__':

    hough_line()                    #直线检测