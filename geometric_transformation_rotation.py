import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
rows,cols,chl = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

b,g,r = cv2.split(img)
img = cv2.merge([r,g,b])
b,g,r = cv2.split(dst)
dst = cv2.merge([r,g,b])
plt.subplot(1,2,1),plt.imshow(img)
plt.subplot(1,2,2),plt.imshow(dst)
plt.show()