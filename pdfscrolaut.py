from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui
from time import sleep
#
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    if lmList:
        bbox = bboxInfo['bbox']
        myHandType = detector.handType()
        cv2.putText(img, f'Hand:{myHandType}', (bbox[0], bbox[1] - 30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        if myHandType == "Right":
            pyautogui.keyDown("PgUp")
            time.sleep(1)

        else:
            pyautogui.keyDown("PgDn")
            time.sleep(1)


    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
