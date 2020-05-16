# import cv2
#
# import sys
#
# cascade_path = "/Users/apple/opt/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"
#
# face_cascade = cv2.CascadeClassifier(cascade_path)
#
# video_capture = cv2.VideoCapture(0)
#
# while True:
#
#     if not video_capture.isOpened():
#         print('Unable to load camera')
#         pass
#
#     ret, frame = video_capture.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     faces = face_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30)
#     )
#
#     for (x,y,w,h) in faces:
#
#         cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
#
#         cv2.imshow('Video', frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#         cv2.imshow('Video', frame)
#
#         video_capture.release()
#
#         cv2.destroyAllWindows()

import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier("/Users/apple/opt/anaconda3/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml")


def face_extractor(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    if faces is():
        return None

    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face



cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        file_name_path = 'faces/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    else:
        print("Face not Found")
        pass

    if cv2.waitKey(1)==13 or count==100:
        break

cap.release()
cv2.destroyAllWindows()
print('Colleting Samples Complete!!!')