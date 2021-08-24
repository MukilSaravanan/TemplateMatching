# Template Matching -Beginner Level
## Python3
 
To run in Command Line Interface (CLI),

```sh
python tm_beginner.py <tm_method> <threshold>
```
For help, type 
```sh
python tm_beginner.py -h
```
usage: ```tm_beginner.py [-h] tm_method threshold```
description: Enter the template matching method with its corresponding threshold value

| positional arguments | Description |
| ------ | ------ |
| tm_method  |0 for Cross Coefficent norm, 1 for Cross Correlation norm, 2 for Square Difference norm |
| threshold | Normalised value [0,1] |


The result image will be stored inside '[images](https://github.com/MukilSaravanan/TemplateMatching/tree/master/beginner_level/images)' directory (i.e. two level up) with the name 'Output_image_<tm_method>_<threshold>.png'
 
**Please read the comments for more information **
 


