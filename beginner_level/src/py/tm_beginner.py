import argparse     #importing for CLI support
import cv2 as cv    #importing computer vision library
import numpy as np  #importing for matrix operations
import os           #importing for manipulating working directory

os.chdir('../../images')    #changing the working directory to there the images are present

class Range(object):        #class definition to restrict floating point numbers within certain range
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start <= other <= self.end

my_parser=argparse.ArgumentParser(description='Enter the template matching method with its corresponding threshold value')      #instantiating argparse 
my_parser.add_argument("Method",metavar='tm_method',type=int,choices=range(0,3),help="0 for Cross Coefficent norm, 1 for Cross Correlation norm, 2 for Square Differnce norm")      #adding template method argument
my_parser.add_argument("Threshold",metavar='threshold',type=float,choices=[Range(0.0, 1.0)],help="Normalised value [0,1]")      #adding threshold value (probability) argument
args=my_parser.parse_args()     #parsing arguments

input_method=args.Method        #getting the template method
input_threshold=args.Threshold      #getting the threshold

methods={0:'cv.TM_CCOEFF_NORMED',1:'cv.TM_CCORR_NORMED',2:'cv.TM_SQDIFF_NORMED'}        #converting numbers to its equivalent method

test_rgb = cv.imread('test_image.png')  #loading the test image
test_gray = cv.cvtColor(test_rgb, cv.COLOR_BGR2GRAY)    #converting the test image into grayscale
template_gray = cv.imread('template_image.png',0)       #loading the template image in grayscale
w, h = template_gray.shape[::-1]        #getting the width and height of the template image

res = cv.matchTemplate(test_gray,template_gray,eval(methods[input_method]))     #template matching with corresponding method
if (input_method!=2):       #finding the locations where the values are in our interest (above or below threshold value)
   loc= np.where( res >= input_threshold)
else:
    loc=np.where( res <= input_threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(test_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,0), 2)      #draw black rectangles with the template image's shape on the test image
cv.imwrite('Output_image_{}_{}.png'.format(methods[input_method],input_threshold),test_rgb)     #storing the output image
cv.imshow("Output_image",test_rgb)      #displaying the output image
cv.imshow("res",res)            #displaying the resultant image
cv.waitKey(0)           #waiting for a key press 
cv.destroyAllWindows()      #destroying all the windows
