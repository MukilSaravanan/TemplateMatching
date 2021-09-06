# TemplateMatching

## Directory structure

```bash
.
├── beginner_level                            
│   ├──images                                     
│   │   ├── *.png                                 #contains the template,test and result images
│   ├──src
│   │   ├── cpp
│   │   │   ├──README.md                          #contains the instructions about complitation, execution of the source code on CLI and others
│   │   │   ├──output                             #binary executable file
│   │   │   ├──tm_beginner.cpp                    #source code
│   │   ├── py
│   │   │   ├──README.md                          #contains the instructions about execution of the source code on CLI and others
│   │   │   ├──tm_beginner.py                     #source code
├── expert_level
│   ├──images
│   │   ├── result_img
│   │   │   ├──*.png                              #contains the result images
│   │   ├── template_img
│   │   │   ├──*.png                              #contains the template images
│   │   ├── test_image.png                        #the test image
│   ├──src
│   │   ├── cpp
│   │   ├── py
│   │   │   ├──.intermittent_dir_for_testing
│   │   │   │   ├──*.py                           #contains the source codes used for intermittent testing 
│   │   │   ├──README.md                          #contains the instructions about execution of the source code on CLI and others
│   │   │   ├──tm_expert.py                       #source code
└──README.md                                      #this file
```

## Template_Matching - Beginner Level - ppy

### Output_image_cv.TM_CCOEFF_NORMED_0.94
![Output_image_cv.TM_CCOEFF_NORMED_0.94](https://github.com/MukilSaravanan/TemplateMatching/blob/master/beginner_level/images/Output_image_cv.TM_CCOEFF_NORMED_0.94.png)
### Output_image_cv.TM_CCORR_NORMED_0.994
![Output_image_cv.TM_CCORR_NORMED_0.994](https://github.com/MukilSaravanan/TemplateMatching/blob/master/beginner_level/images/Output_image_cv.TM_CCORR_NORMED_0.994.png)
### Output_image_cv.TM_SQDIFF_NORMED_0.02
![Output_image_cv.TM_SQDIFF_NORMED_0.02](https://github.com/MukilSaravanan/TemplateMatching/blob/master/beginner_level/images/Output_image_cv.TM_SQDIFF_NORMED_0.02.png)


## Template_Matching - Beginner Level - cpp
### cv::TM_CCOEFF_NORMED
![Final](https://github.com/MukilSaravanan/TemplateMatching/blob/master/beginner_level/images/Final.png)

## Template_Matching - Expert level - py
### cv2.TM_CCOEFF, Multi-Scale template matching
![mstm1_out](https://github.com/MukilSaravanan/TemplateMatching/blob/master/expert_level/images/result_img/mstm1_out.png)
