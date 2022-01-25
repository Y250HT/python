import cv2

def capture_camera():
    # 获取第0个摄像头
    cap = cv2.VideoCapture(0)
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
            # 等待30毫秒，等用户输入按键，若用户按了q键，则退出
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
    # 释放摄像头
    cap.release()
    cv2.destroyAllWindows()

capture_camera()