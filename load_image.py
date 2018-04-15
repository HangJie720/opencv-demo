import numpy as np
import cv2

# Load a color imge in grayscale
img = cv2.imread('butterfly.jpg',flags=cv2.IMREAD_GRAYSCALE)

# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:               # Wait for Esc to Exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messigray.jpg', img)
    cv2.destroyAllWindows()