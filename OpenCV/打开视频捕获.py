import cv2
def play_video_file():
    path = 'D:/2022_Work/计算机设计大赛/课程讲解/2/'
    # 打开视频文件
    cap = cv2.VideoCapture(path + 'vid.mp4')
    while True:
        # 读取一帧
        ret, frame = cap.read()
        # 若未读取成功，则文件不存在或者文件已经播放完毕，退出循环
        if not ret:
            break
        else:
            # 读取成功，则显示这一帧
            cv2.imshow('preview', frame)
            # 等待30毫秒，等用户输入按键，若用户按了q键，则退出
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
    # 释放视频文件
    cap.release()
    # 关闭所有窗口
    cv2.destroyAllWindows()

play_video_file()