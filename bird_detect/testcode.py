import cv2
import numpy as np
cap = cv2.VideoCapture(0)
ix, iy = -1,-1

def mouseCallback(event,x,y,flags,param):
    global ix
    global iy

    if event == cv2.EVENT_LBUTTONDOWN:
        ix = x # saves the position of the last click
        iy = y

    elif event == cv2.EVENT_LBUTTONUP:
        print("EVENT_LBUTTONUP")

    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Appuyé Droite")

    elif event == cv2.EVENT_RBUTTONUP:
        print("EVENT_RBUTTONUP")

def draw_circle_onscreen(frame, x,y):

    cv2.circle(frame, (0, 0), 100, (0, 0, 255), 1)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',mouseCallback) # mouse callback has to be set only once

while(1):
    ret, img = cap.read()
    draw_circle_onscreen(img,ix,iy) # draws circle on screen
    cv2.imshow('frame',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()