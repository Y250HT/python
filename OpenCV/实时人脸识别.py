import cv2
def capture_camera():
    cap = cv2.VideoCapture(0)
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    while True:
        ret, frame = cap.read()
        if not ret:
            print("no video capture device")
            break
        else:
            gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray,
                                                   scaleFactor=1.1,
                                                   minNeighbors=10)
            for x,y,w,h in faces:
                cv2.rectangle(frame,
                              pt1 = (x,y),
                              pt2 = (x+w,y+h),
                              color=[0,0,255],
                              thickness=2)
            cv2.imshow('preview', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

capture_camera()
