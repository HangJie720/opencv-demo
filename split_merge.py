import numpy as np
import cv2

img = cv2.imread('butterfly.jpg')
b,g,r = cv2.split(img)   # b = img[:,:,0]
img = cv2.merge((b,g,r))
