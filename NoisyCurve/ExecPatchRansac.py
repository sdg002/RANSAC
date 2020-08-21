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


def run(inputfilename):
    folder_script=os.path.dirname(__file__)
    file_noisy_circle=os.path.join(folder_script,"./in/",inputfilename)
    np_image=skimage.io.imread(file_noisy_circle,as_gray=True)

    
    patcher=PatchRansacHelper()
    patcher.OutputImageFile=create_new_absolute_filename(inputfilename)
    patcher.run(np_image)
    pass


def stride_across(image):
    pass

def create_new_absolute_filename(inputfile):
    prefix=os.path.splitext(inputfile)[0]
    folder_script=os.path.dirname(__file__)
    folder_results=os.path.join(folder_script,"./out/")
    count_of_files=len(os.listdir(folder_results))
    new_filename=("%s.%d.results.png" % (prefix,count_of_files))
    file_result=os.path.join(folder_script,"./out/",new_filename)
    return file_result

run("Sine-W=500.H=200.MAXD=20.SP=0.95.0.png")

