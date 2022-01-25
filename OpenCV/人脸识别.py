import numpy as np
import cv2
if __name__ == '__main__':
    img = cv2.imread('zcr.webp')
    # 使用灰色的图像效果更好，因为两者大小一样，故可以
    gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
    # 级联分类器CasscadeClassifier
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    faces = face_detector.detectMultiScale(gray,
                                           scaleFactor=1.05, # 缩放，默认1.1
                                           minNeighbors=3) # 返回坐标
    # 同时可以指定最小尺寸minsize
    print(faces)
    #  w宽度，h高度
    for x,y,w,h in faces:
        cv2.rectangle(img,
                      pt1=(x, y), pt2=(x+w, y+h),
                      color=[0, 0, 255],
                      thickness=2)
    cv2.imshow('zcr', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
