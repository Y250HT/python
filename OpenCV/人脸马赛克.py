import numpy as np
import cv2
if __name__ =='__main__':
    img = cv2.imread('wbq.webp')
    # 人脸坐标（0，220），（300，470）
    face = img[:300, 220:470]
    # 对人脸进行马赛克在放大
    # 无论行列均间隔10取一个像素，都放大
    face = face[::10, ::10]
    face = np.repeat(face, 10, axis=0)
    face = np.repeat(face, 10, axis=1)
    # 再贴到原图上
    img[:300, 220:470] = face
    cv2.imshow('bao', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()