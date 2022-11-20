from pyzbar.pyzbar import decode
import cv2
import numpy as np
import time

# img = cv2.imread('1.png')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

used_code = []

while True:

    success, img = cap.read()
    for qr in decode(img):
        myData = qr.data.decode('UTF-8')  # convets to str
        if qr.data.decode('UTF-8') not in used_code:
            print(qr.data)
            print(myData)
            pts = np.array([qr.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 200), 2)
            pts2 = qr.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 0, 200), 2)
            used_code.append(myData)
            time.sleep(1)
        elif qr.data.decode('UTF-8') in used_code:
            pts = np.array([qr.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(img, [pts], True, (255, 0, 200), 2)
            pts2 = qr.rect
            cv2.putText(img, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_PLAIN, 0.9, (255, 0, 200), 2)
            print("Alreay seen, try a different qr.")
            time.sleep(0)
        else:
            pass
        if len(used_code) == 5:
            print(used_code)
        else:
            pass
        cv2.imshow("results", img)
        cv2.waitKey(1)
