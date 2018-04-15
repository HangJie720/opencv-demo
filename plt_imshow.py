import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load grayscale image
img = cv2.imread('butterfly.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray',interpolation='bicubic')
plt.xticks([]),plt.yticks([])   # to hide tick values on X and Y axis
plt.show()

# Load RGB image
img = cv2.imread('butterfly.jpg')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img)
plt.subplot(122);plt.imshow(img2)
plt.xticks([]),plt.yticks([])   # to hide tick values on X and Y axis
plt.show()

