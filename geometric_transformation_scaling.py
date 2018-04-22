import cv2

img = cv2.imread('messi5.jpg')
res1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

# OR
height, width = img.shape[:2]
res2 = cv2.resize(img,(2*height,2*width),interpolation=cv2.INTER_CUBIC)

cv2.imshow('res1',res1)
cv2.waitKey(0)
cv2.destroyAllWindows()