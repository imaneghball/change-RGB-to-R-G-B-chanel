import cv2
import numpy as np
farbImg=cv2.imread("lena.ppm")
blue=np.zeros(farbImg.shape,dtype="uint8")
grün=np.zeros(farbImg.shape,dtype="uint8")
rot=np.zeros(farbImg.shape,dtype="uint8")
for i in range(farbImg.shape[0]):
    for j in range(farbImg.shape[1]):
        blue[i,j][0]=farbImg[i,j][0]
        grün[i, j][1] = farbImg[i, j][1]
        rot[i, j][2] = farbImg[i, j][2]
cv2.imwrite("blue.jpg",blue)
cv2.imwrite("grün.jpg",grün)
cv2.imwrite("rot.jpg",rot)
cv2.imwrite("lena.jpg",farbImg)
outPut=np.hstack([np.vstack([farbImg,blue]),np.vstack([grün,rot])])
cv2.imshow("output",outPut)
while True:
    key=cv2.waitKey(0) & 0xFF
    if key==27: break