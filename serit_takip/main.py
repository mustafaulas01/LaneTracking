import cv2
import numpy as np

img1 = cv2.imread("serit_takip/images/path.jpg")
img = cv2.imread("serit_takip/images/path.jpg")


hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
sensitivity = 70
lower_white = np.array([0,0,255-sensitivity])
upper_white = np.array([255,sensitivity,255])
mask = cv2.inRange(hsv,lower_white,upper_white)
res = cv2.bitwise_and(img,img,mask=mask)


edges = cv2.Canny(res,2,6)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50)

for line in lines:
    (x1,y1,x2,y2) = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("Orijin",img1)
cv2.imshow("res",res)
cv2.imshow("img",img)





cv2.waitKey(0)
cv2.destroyAllWindows()
