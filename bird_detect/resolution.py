import numpy as np
import cv2
cap = cv2.VideoCapture(0)
print(cap.get(3), cap.get(4))
ret = cap.set(3,1000)
ret = cap.set(4,1000)


while(True):

    ret, frame = cap.read()
    cv2.circle(frame, (250, 250), 100, (0, 0, 255), 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()