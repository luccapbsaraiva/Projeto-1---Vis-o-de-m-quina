import cv2
import numpy as np
import matplotlib.pyplot as plt
from Projeto import *

boa_rgb = cv2.cvtColor(boa2, cv2.COLOR_BGR2RGB)

def verifica_amassada(img):
    params = cv2.SimpleBlobDetector_Params()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY)


    #contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(boa_rgb, contours, -1, (0,0,255), 2)



    # Set blob color (0=black, 255=white)
    params.filterByColor = True
    params.blobColor = 0
    # Filter by Area
    params.filterByArea = True
    params.minArea = 100
    params.maxArea = 100000


    # Filter by Circularity
    params.filterByCircularity = False
    params.minCircularity = 0.2
    params.maxCircularity = 1.2
    # Filter by Convexity
    params.filterByConvexity = False
    #params.minConvexity = 0.87
    #params.maxConvexity = 1
    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.30
    params.maxInertiaRatio = 1


    detector = cv2.SimpleBlobDetector_create(params)

    KP = detector.detect(thresh)
    print(len(KP))
    for KPi in KP:
        centro_x = KPi.pt[0]
        centro_y = KPi.pt[1]

    return thresh


fig = plt.figure(figsize=(10,10))
fig.add_subplot(1,2,1)
plt.imshow(verifica_amassada(boa2), cmap='gray')
fig.add_subplot(1,2,2)
plt.imshow(boa_rgb)
plt.show()
