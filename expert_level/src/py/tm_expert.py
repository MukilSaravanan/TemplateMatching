import numpy as np      #importing for matrix operations
import imutils          #importing for image manipulations
import glob             #importing for working with files in different directories
import cv2              #importing computer vision library

image = cv2.imread("../../images/test_image.png")       #loading the test image

for templatePath in glob.glob("../../images/tm_imgs"+"/*.png"):     #iterating over the template images

    template = cv2.imread(templatePath,0)     #loading the template image as grayscale
    template = imutils.resize(template,height=100,width=150)      #resizing the template image
    template = cv2.Canny(template, 100, 200)        #canny edge detector
    (tH, tW) = template.shape[:2]       #getting the template's dimension
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)      #converting the test image into grayscale
    found = None        #found flag for finding the max value

    for scale in np.linspace(0.2, 1.0, 20)[::-1]:       #iterating over different resize values
        resized = imutils.resize(gray, width = int(gray.shape[1] * scale))      #resizing the test image
        r = gray.shape[1] / float(resized.shape[1])     #finding the aspect ratio

        if resized.shape[0] < tH or resized.shape[1] < tW:      #break out of the loop immediately if the test image's dimension is lesser than template image's dimension
            break

        edged = cv2.Canny(resized,  50, 200)        #canny edge dectection for test image
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)      #template matching with cross coefficient method
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)      #finding the maximum value and its corresponding location

        if found is None or maxVal > found[0]:      #if this is the first time or higher value than the previous maximum value
            found = (maxVal, maxLoc, r)     #assign the new maximum value,its corresponding location 

    (_, maxLoc, r) = found      #unpacking the final values 
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))         #finding the dimension of the bounding box to be drawn
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)        #drawing the bounding box in red 
    cv2.imwrite('../../images/result_img/mstm1_out.png',image)      #saving the result image

cv2.imshow("Image", image)      #displaying the result image
cv2.waitKey(0)      #waiting for a key press
cv2.destroyAllWindows()     #destroying all the windows
