import numpy as np
import cv2

# Load a color imge in grayscale
img = cv2.imread('messi5.jpg')
print img.shape
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:               # Wait for Esc to Exit
    cv2.destroyAllWindows()
elif k == ord('s'):
    a = img[220:280, 260:320]
    img[140:200, 350:410] = a
    cv2.imwrite('messi5modify.jpg', img)
    cv2.destroyAllWindows()