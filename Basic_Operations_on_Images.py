import numpy as np
import cv2

img = cv2.imread('messi5.jpg')

# Access the properties of image
print(img.shape)
print(img.size)
print(img.dtype)
# Access the pixel of image
px = img[100,100]
print(px)

# Access only the blue pixel

# px = img[100,100,0]
# print(px)
print img.item(100,100,2)

# Modify the pixel value

# img[100,100]=[255,255,255]
# print(img[100,100])
img.itemset((100,100,2),100)
print img.item(100,100,2)