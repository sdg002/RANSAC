from RANSAC.Algorithm import PatchRansacHelper
from RANSAC.Common import LineModel
from RANSAC.Common import Point
from RANSAC.Common import Util

import skimage
import os
import datetime
import sys
from skimage.transform import rescale, resize, downscale_local_mean
import os


def run(filename):
    folder_script=os.path.dirname(__file__)
    file_noisy_circle=os.path.join(folder_script,"./in/",filename)
    np_image=skimage.io.imread(file_noisy_circle,as_gray=True)

    #####

    #folder_script=os.path.dirname(__file__)
    #folder_results=os.path.join(folder_script,"./out/")

    #width=np_image.shape[1]
    #height=np_image.shape[0]

    #np_image_top_left=np_image[0:int(height/2),0:int(width/2)]
    #file_result_top_left=os.path.join(folder_script,"./out/","top_left.png")
    #skimage.io.imsave(file_result_top_left,np_image_top_left)

    #np_image_top_right=np_image[0:int(height/2),int(width/2):width]
    #file_result_top_right=os.path.join(folder_script,"./out/","top_right.png")
    #skimage.io.imsave(file_result_top_right,np_image_top_right)


    #####
    #image_rescaled = rescale(np_image, 0.25, anti_aliasing=False)

    
    #YOU WERE HERE, SAVE THE IMAGE AND SEE THE RESULTS
    #BUT THIS IS NTO WHAT YOU WANT TO DO YOU WANT TO STRIDE ACROSS
    patcher=PatchRansacHelper()
    patcher.run(np_image)
    pass


def stride_across(image):
    pass


run("Sine-W=500.H=200.MAXD=20.SP=0.95.0.png")

