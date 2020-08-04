import numpy as np
import os
import skimage
import random

from RANSAC.Common import LineModel
from RANSAC.Common import Point
from RANSAC.Common import Util


#
#Create blank image
#
img_back_color=255
img_width=200
img_height=200
salt_pepper_noise=.95 #0.2 Temporary
print("This script will create a monochrome image (100X50) consisting of a random line and salt-pepper noise")
img = np.zeros([img_height,img_width,1],dtype=np.uint8)
img.fill(img_back_color)
#
#Generate Salt-Pepper noise
#
image_noisy=skimage.util.random_noise(img,mode="s&p",seed=None, clip=True,salt_vs_pepper=salt_pepper_noise)
#
#Save the image to disk
#
image_result=image_noisy
folder_script=os.path.dirname(__file__)
folder_results=os.path.join(folder_script,"./out/")
count_of_files=len(os.listdir(folder_results))
filename=("NoisyCurve-Gaussian-sp-%.2f.%d.png" % (round(salt_pepper_noise,2),count_of_files))
file_result=os.path.join(folder_script,"./out/",filename)
skimage.io.imsave(file_result,image_result)
print("Image saved to fileL%s" % (file_result))


