
import cv2, time

video = cv2.VideoCapture(0)
first_frame = None
while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray)

    if first_frame == None:
        first_frame = gray
        continue

    cv2.imshow('capturing', gray)

    key = cv2.waitKey(1)
    print(gray)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()