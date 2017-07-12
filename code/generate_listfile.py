import os
from PIL import Image
from os import listdir
from resizeimage import resizeimage
import glob

basePath = '/Users/abhaydoke/Documents/Courses/deep-learning-final-project/food datasets/food-101/data/'

classes = listdir(basePath)

f = open("/Users/abhaydoke/Documents/Courses/deep-learning-final-project/food datasets/food-101/listfile.txt", "w")
classCounter = 0
for className in classes:
	classInDirPath = basePath+'/'+className
	
	
	classImages = glob.glob(classInDirPath+'/*.jpg')
	
	
	for imageName in classImages:
		imageName = imageName.split('/')[-1]
		f.write(className+'/'+imageName+' '+str(classCounter)+'\n')
	classCounter = classCounter+1
f.close()
