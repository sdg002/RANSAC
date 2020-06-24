#
#Use this script to generate a mono chrome picture with 1 circle and noise
#This will generate a random circle line
#  *)select a random radius from 0.5 diagonal to 1.0 diagonal
#  *)select a random center from left-0.25*radius,right+0.25*radius
#  *)
#

import numpy as np
import os
import skimage
from RANSAC.Common import Util
from RANSAC.Common import CircleModel
from RANSAC.Common import Point
import random
import math
#
#Create blank image
#
img_white_color=255
img_width=100
img_height=100
salt_pepper_ratio=0.2

print("This script will create a monochrome image (%d X %d) consisting of a partial circle and salt-pepper noise",img_width,img_height)
img = np.zeros([img_height,img_width,1],dtype=np.uint8)
img.fill(img_white_color)

#
#Generate Salt-Pepper noise
#
image_noisy=skimage.util.random_noise(img,mode="s&p",seed=None, clip=True,salt_vs_pepper=salt_pepper_ratio)
#
#Generate circle
#
center_x=-img_width*0.5 + 2*img_width*random.random()
center_y=-img_height*0.5 + 2*img_height*random.random()
radius=(img_width+img_height)/3.0 * (1+random.random())
density=0.5
def generate_points_for_circle(centerx,centery,r,density_factor):
    pts_on_circle=[]
    num_points=int(2*3.141*r*density_factor)  #proportional to circumfrence
    angles=np.linspace(0,2.0*3.141,num_points)
    for angle in angles:
        x=math.sin(angle)*r+centerx
        y=math.cos(angle)*r+centery
        newpoint=Point(x,y)
        pts_on_circle.append(newpoint)
    return pts_on_circle
    pass

print("Generating noisy circle at center (x,y,radius) (%d,%d,%d)" % (center_x,center_y,radius))
lst_circle=generate_points_for_circle(center_x,center_y,radius,density)
image_result=Util.superimpose_points_on_image(image_noisy,lst_circle,0,0,255)


#
#Save the image to disk
#
folder_script=os.path.dirname(__file__)
folder_results=os.path.join(folder_script,"./out/")
count_of_files=len(os.listdir(folder_results))

filename="NoisyCircle_x_%d_y_%d_r_%d_d_%f.%d.png" % (center_x,center_y,radius,density,count_of_files)
file_result=os.path.join(folder_script,"./out/",filename)
skimage.io.imsave(file_result,image_result)
print("Image saved to fileL%s" % (file_result))
