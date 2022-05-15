import cv2
import numpy as np
import pyautogui


#size of the window
SCREEN_SIZE = (1920, 1080)

#start application
fourcc = cv2.VideoWriter_fourcc(*"XVID")

#output
output = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destoryAllWindow()
output.release()
