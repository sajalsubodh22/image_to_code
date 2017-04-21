from scipy import misc
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.cm as cm 
from PIL import Image,ImageEnhance, ImageFilter
from pytesseract import image_to_string
import os
'''
def average(pixel):
	return np.average(pixel)
'''


def image_enhance(img):
	#set dpi to 600,600
	image = Image.open(img)
	
	dir = os.getcwd()+"/enhanced_test"
	os.chdir(dir)
	#image.save('image_600.jpg',dpi=(600,600))

	#image enhacement
	#image = Image.open('image_600.jpg')
	image = image.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Sharpness(image)
	factor = 2.0
	image = enhancer.enhance(factor)

	#grey scale
	coloriser = ImageEnhance.Color(image)
	factor = 0.0
	image = coloriser.enhance(factor)

	#contrast setting
	coloriser = ImageEnhance.Contrast(image)
	image.save('image_enhanced.jpg')

	code = image_to_string(Image.open('image_enhanced.jpg'))
	return  code


'''
#Grey scale conversion
image  = misc.imread('test2-600.jpg')
print image.shape

grey = np.zeros((image.shape[0], image.shape[1])) # init 2D numpy array
# get row number
for rownum in range(len(image)):
   for colnum in range(len(image[rownum])):
      grey[rownum][colnum] = average(image[rownum][colnum])


plt.imshow(grey, cmap = cm.Greys_r)
plt.show()


misc.imsave('test2-grey.jpg',grey)

code = image_to_string(Image.open('test2-grey.jpg'))
print code
'''