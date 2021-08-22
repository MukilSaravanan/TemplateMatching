import numpy as np
import cv2 as cv
import imutils

template=cv.imread("../../images/choco_pie_top.png")
cv.imshow("Template",template)
print("template size:",template.shape)

resized=imutils.resize(template,width=100)
cv.imshow("Resized",resized)
cv.imwrite("resize_template.png",resized)
print("resized template size:",resized.shape)

image=cv.imread("../../images/test_image.png",0)
cv.imshow("Image",image)
print(" Image size:",image.shape)

canny_template=cv.Canny(resized,50,200)
cv.imshow("Canny Template",canny_template)

matched_image=cv.matchTemplate(image,canny_template,cv.TM_CCOEFF_NORMED)
cv.imshow("Matched Image",matched_image)

cv.waitKey(0)
cv.destroyAllWindows()

