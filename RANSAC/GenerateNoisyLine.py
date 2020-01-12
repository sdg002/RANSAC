import numpy as np


import numpy as np
import os
import skimage
img_width=100
img_height=50
img = np.zeros([img_height,img_width,1],dtype=np.uint8)
folder_script=os.path.dirname(__file__)
lst_colors=[100,150,200,255]
for color in lst_colors:
    filename="Numpy.BlankImage.%d.png" % color
    file_result=os.path.join(folder_script,"./out/",filename)
    img.fill(color)
    skimage.io.imsave(file_result,img)

