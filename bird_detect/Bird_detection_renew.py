import cv2
import numpy as np

bird1_cascade = cv2.CascadeClassifier('bird1-cascade.xml')
bird2_cascade = cv2.CascadeClassifier('bird2-cascade.xml')

cap = cv2.VideoCapture(0)
count = 0
# cap = cv2.imread('/Users/apple/PycharmProjects/Project_satellite/bird_detect/1.jpg')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(3)
height = cap.get(4)

# height, width = cap.shape

ix, iy = width/2,height/2

def draw_circle_onscreen(frame, x,y):
    cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)  # Red Dot
    cv2.circle(frame, (x, y), 45, (0, 0, 255), 1) # Red
    cv2.circle(frame, (x,y), 90,(0,0,255), 1) # Blue Circle
    cv2.circle(frame, (x, y), 180, (0,0,255), 1) # Green Circle




while 1:

    ret, img = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    draw_circle_onscreen(img, int(width / 2), int(height / 2))  # draws circle on screen
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    birds1 = bird1_cascade.detectMultiScale(gray, 1.8, 5)
    birds2 = bird2_cascade.detectMultiScale(gray, 1.8, 5)

    for (x, y, w, h) in birds1:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
        # a = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        count = 1

    for (x, y, w, h) in birds2:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, '', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
        count = 1

    if count >= 1:
        cv2.putText(img, '', (x - w, y - h), font, 0.5, (255, 255, 0), 2)

    count = 0

    cv2.imshow('img', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
