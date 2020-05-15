# ㅂㅏㄴ복적 처리 알고리
#-*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

a = np.random.randint(25,50,(25,2))
b = np.random.randint(55,85,(25,2))

z = np.vstack((a,b))

z=np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

flags = cv2.KMEANS_RANDOM_CENTERS

compactness,labels,centers = cv2.kmeans( z, 2, criteria, 10, flags)

A = z[labels.ravel()==0]
B = z[labels.ravel()==1]

plt.scatter(A[:, 0], A[:, 1], c='b')
plt.scatter(B[:, 0], B[:, 1], c='r')
plt.scatter(centers[:, 0], centers[:, 1], s=80, c='y', marker='s')

plt.xlabel('Height')
plt.ylabel('Weight')
plt.show()