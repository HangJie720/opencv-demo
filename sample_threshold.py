import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gradient.png',0)
retv,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
retv,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
retv,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
retv,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
retv,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()