import numpy as np
import cv2


# 컬러 이미지를 저장할 넘파이 배열을 생성합니다.
width = 500
height = 500
bpp = 3

cap = cv2.VideoCapture(0)


# (250,250)이 중심인 반지름 10인 파란색으로 채워진 원을 그립니다.
cv2.circle(cap, (250, 250), 10, (255, 0, 0), -1)

# (250,250)이 중심인 반지름이 100인 선굵기가 1인 빨간색 원을 그립니다.
cv2.circle(cap, (250, 250), 100, (0, 0, 255), 1)


cv2.imshow("result", cap)
cv2.waitKey(0);
#
# import cv2
# import numpy as np
#
# white_coloc = (255,255,255)
#
# cap = cv2.VideoCapture(0)
# cap = cv2.circle()
#
# cap.release()
# cv2.destroyAllWindows()