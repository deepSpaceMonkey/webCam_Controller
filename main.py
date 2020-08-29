import cv2
import numpy as np


capture = cv2.VideoCapture(0)

blue_lower=np.array([100,150,0],np.uint8) # RGB combo
blue_upper=np.array([140,255,255],np.uint8)

while True:
    ret, frame = capture.read()    # We need this inside the while loop to get multiple frames (video)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    # Convert camera image to black and white so more contrast for the blue object. Easier detetction
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, blue_lower, blue_upper)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 40000:    # Much less "noise". Anything that is smaller than object size does not get registered
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame)
            # cv2.drawContours(frame, c, -1, (0, 255, 0), 2)    # Will draw around the object, to be used in scrolling

    cv2.imshow('frame', frame)
   #  cv2.imshow('mask', mask)

    if cv2.waitKey(10) == ord('q'):    # 'q' for quit
        break

capture.release()
cv2.destroyAllWindows()
