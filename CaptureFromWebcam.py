import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
out = cv2.VideoWriter('output2.avi', cv2.cv.CV_FOURCC('M','J','P','G'), 25, 
               (640,480),True)



while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
       # frame = cv2.flip(frame,0) to flip the frame upside down, why would anyone do that though?

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()