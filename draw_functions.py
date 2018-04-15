import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3),np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a green rectangle at the top-right of image with thickness of 2px
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# To draw a circle, you need its center coordinates and radius. We will draw a circle inside the rectangle drawn above.
img = cv2.circle(img,(447,63),63,(0,0,255),-1)

# Draw ellipse
img = cv2.ellipse(img,(256,256),(50,50),0,0,315,(0,255,0),-1)
img = cv2.ellipse(img,(256,256),(20,20),0,0,315,(0,0,0),-1)

# Draw polygon
pts = np.array(([10,5],[20,30],[70,20],[50,10]),np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

# Add text to images

img = cv2.putText(img,'OpenCV',(10,500),cv2.FONT_HERSHEY_COMPLEX,4,(255,255,255),2,cv2.LINE_AA)
cv2.imwrite('image.jpg',img)

image = cv2.imread('image.jpg')
cv2.imshow('image',image)
k = cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()