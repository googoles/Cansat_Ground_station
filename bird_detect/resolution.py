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

# import cv2
# import numpy as np
#
# bird1_cascade = cv2.CascadeClassifier('bird1-cascade.xml')
# bird2_cascade = cv2.CascadeClassifier('bird2-cascade.xml')
# cap = cv2.VideoCapture('bird2.mp4')
# count = 0
# while 1:
#
#     ret, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     birds1 = bird1_cascade.detectMultiScale(gray, 1.2, 5)
#     birds2 = bird2_cascade.detectMultiScale(gray, 1.2, 5)
#     for (x, y, w, h) in birds1:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, 'Warning', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
#         a = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         count = 1
#     for (x, y, w, h) in birds2:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         cv2.putText(img, 'Warning', (x - w, y - h), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
#         count = 1
#     if count >= 1:
#         cv2.putText(img, 'Warning', (x - w, y - h), font, 0.5, (255, 255, 0), 2, cv2.LINE_8)
#     print(count)
#     count = 0
#     cv2.imshow('img', img)
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# cap.release()
# cv2.destroyAllWindows()