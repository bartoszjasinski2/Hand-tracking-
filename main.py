import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

width, height = 1280, 720

#kamera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

previousTime = 0
currentTime = 0
#wykrywanie dłoni
hand_detector = HandDetector(maxHands = 1, detectionCon= 0.8)

#wysyłanie do unity
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddresPort = ("127.0.0.1",5052)

while True:
    # wczytywanie obrazu z kamery klatka po klatce
    success, frame = cap.read()
    # wykrywanie dłoni
    hands, frame = hand_detector.findHands(frame)
    data_frame = []
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime+
    if hands:
        hand = hands[0]
        lm_list = hand["lmList"]
        mark0 = lm_list[0]
        mark5 = lm_list[5]
        mark0_center = (mark0[0],mark0[1])
        mark5_center = (mark5[0],mark5[1])
        cv2.circle(frame, mark0_center,5, (214, 9, 187),cv2.FILLED)
        cv2.circle(frame, mark5_center,5, (214, 9, 187), cv2.FILLED)
        cv2.line(frame,mark0_center,mark5_center,(9, 223, 235),3)
        w,_ = hand_detector.findDistance(mark0_center,mark5_center)
        for lm in lm_list:
            data_frame.extend([lm[0], height - lm[1], lm[2]])
        print(data_frame)
        sock.sendto(str.encode(str(data_frame)),serverAddresPort)
    frame = cv2.resize(frame,(0,0),None,0.5,0.5)
    cv2.putText(frame, str(int(fps)) + " FPS", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Image", frame)
    cv2.waitKey(1)