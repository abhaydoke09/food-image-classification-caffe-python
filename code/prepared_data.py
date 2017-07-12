import os
from PIL import Image
from os import listdir
from resizeimage import resizeimage
import glob


basePath = '/Users/abhaydoke/Documents/Courses/deep-learning-final-project/food datasets/food-101/images'
outputPath = '/Users/abhaydoke/Documents/Courses/deep-learning-final-project/food datasets/food-101/processed/'

classes = listdir('/Users/abhaydoke/Documents/Courses/deep-learning-final-project/food datasets/food-101/images')

for className in classes:
	classInDirPath = basePath+'/'+className
	classOutDirPath = outputPath+'/'+className
	if not os.path.exists(classOutDirPath):
		os.makedirs(classOutDirPath)


	classImages = glob.glob(classInDirPath+'/*.jpg')
	imageCounter = 1
	for imageName in classImages:
		#print imageName
		with open(imageName, 'r+b') as f:
			with Image.open(f) as image:
				cover = resizeimage.resize_cover(image, [256, 256])
				cover.save(outputPath+className+'/'+str(imageCounter)+'.jpg', image.format)
        		imageCounter+=1

	print className+ ' Done..'