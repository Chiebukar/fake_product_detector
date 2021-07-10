import cv2
import numpy as np
from pyzbar.pyzbar import decode

# image = cv2.imread('search.jpg')
cap = cv2.VideoCapture(0)
# cap.set(3, 2500), cap.set(4, 2000)
cap.set(3, 640), cap.set(4, 480)
while True:
    ret, frame = cap.read()
    try:
        for code in decode(frame):
            data = code.data.decode('utf-8')
            polyPoints = np.array([code.polygon], np.int32)
            polyPoints= polyPoints.reshape(-1, 1, 2)
            cv2.polylines(frame, polyPoints, True, (255, 0, 255), 1,)
            rectPoints = code.rect
            cv2.putText(frame, data, (rectPoints[0], rectPoints[1]), cv2.FONT_HERSHEY_PLAIN,
                                      1, (255, 0, 255), 2)
    except Exception as e:
        print(e)
   
    cv2.imshow('video', frame)
    cv2.waitKey(1)
