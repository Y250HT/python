import cv2
def capture_save_image():
    path = "D:/2022_Work/Code/Python/OpenCV/pic_get/"           #禁止中文路径保存
    path2="D:/2022_Work/计算机设计大赛/课程讲解/2/vid2.mp4"
    # 获取第0个摄像头
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(path2)
    while True:
        # 读取一帧
        ret, frame = cap.read()
        # 若未读取到（没有摄像头）
        if not ret:
            print('no video capture device')
            break
        else:
            # 若读取到了视频，则显示
            cv2.imshow('preview', frame)
            # 等待30毫秒，等用户输入按键
            key = cv2.waitKey(1)
            # 若用户按了p键，则截图（将当前帧保存）
            if key & 0xFF == ord('p'):
                cv2.imwrite(path + 'get_ok.jpg', frame)
            # 等用户输入按键，若用户按了q键，则退出
            elif key & 0xFF == ord('q'):
                break
    # 释放摄像头
    cap.release()
    cv2.destroyAllWindows()

capture_save_image()