import numpy as np


import numpy as np
import os
import skimage
#
#Create blank image
#
img_back_color=255
img_width=100
img_height=50
img = np.zeros([img_height,img_width,1],dtype=np.uint8)
img.fill(img_back_color)
#
#Generate Salt-Pepper noise
#
image_noisy=skimage.util.random_noise(img,mode="s&p",seed=None, clip=True,salt_vs_pepper=0.2)
#
#Save the image to disk
#
folder_script=os.path.dirname(__file__)
filename="Numpy.BlankImage.%d.png" % img_back_color
file_result=os.path.join(folder_script,"./out/",filename)
skimage.io.imsave(file_result,image_noisy)
#
#
#
