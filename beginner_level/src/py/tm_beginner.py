import argparse
import cv2 as cv
import numpy as np
import os
os.chdir('../../images')

class Range(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __eq__(self, other):
        return self.start <= other <= self.end

my_parser=argparse.ArgumentParser(description='Enter the template matching method with its corresponding threshold value')
my_parser.add_argument("Method",metavar='tm_method',type=int,choices=range(0,3),help="0 for Cross Coefficent norm, 1 for Cross Correlation norm, 2 for Square Differnce norm")
my_parser.add_argument("Threshold",metavar='threshold',type=float,choices=[Range(0.0, 1.0)],help="Normalised value [0,1]")
args=my_parser.parse_args()

input_method=args.Method
input_threshold=args.Threshold

methods={0:'cv.TM_CCOEFF_NORMED',1:'cv.TM_CCORR_NORMED',2:'cv.TM_SQDIFF_NORMED'}


test_rgb = cv.imread('test_image.png')
test_gray = cv.cvtColor(test_rgb, cv.COLOR_BGR2GRAY)
template_gray = cv.imread('template_image.png',0)
w, h = template_gray.shape[::-1]


res = cv.matchTemplate(test_gray,template_gray,eval(methods[input_method]))
loc = np.where( res >= input_threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(test_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,0), 2)
    
cv.imwrite('Output_image.png',test_rgb)
cv.imshow("Output_image",test_rgb)
cv.imshow("res",res)
cv.waitKey(0)  
cv.destroyAllWindows()
