import numpy as np
import os
import skimage
import random
import math

from RANSAC.Common import LineModel
from RANSAC.Common import Point
from RANSAC.Common import Util
from GenericCurveGenerator import GenericCurveGenerator



#
#Create blank image
#
img_back_color=255
img_width=500
img_height=200
salt_pepper_noise=.95
max_distance_between_2_points=10
#20 becomes too large with sp=0.95

def create_new_absolute_filename(prefix):
    folder_script=os.path.dirname(__file__)
    folder_results=os.path.join(folder_script,"./out/")
    count_of_files=len(os.listdir(folder_results))
    new_filename=("%s.%d.png" % (prefix,count_of_files))
    file_result=os.path.join(folder_script,"./out/",new_filename)
    return file_result

generator=GenericCurveGenerator(width=img_width,height=img_height)
generator.saltpepper=salt_pepper_noise
generator.output_file=create_new_absolute_filename("Sine")
generator.generate_curve()
pass
