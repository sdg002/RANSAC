import numpy as np
import os
import skimage
import random
import math

from RANSAC.Common import LineModel
from RANSAC.Common import Point
from RANSAC.Common import Util



#
#Create blank image
#
img_back_color=255
img_width=500
img_height=200
salt_pepper_noise=.95
max_distance_between_2_points=10
#20 becomes too large with sp=0.95

#
#Generate Salt-Pepper noise
#
def generate_blankimage_with_saltpepper_noise(width,height,saltpepper_noise):
    print("This script will create a monochrome image (100X50) consisting of a random line and salt-pepper noise")
    img = np.zeros([height,width,1],dtype=np.uint8)
    img.fill(img_back_color)
    image_noisy=skimage.util.random_noise(img,mode="s&p",seed=None, clip=True,salt_vs_pepper=saltpepper_noise)
    return image_noisy

#
#Save the image to disk
#
def save_image_to_disk(image_array,filename):
    image_result=image_array
    folder_script=os.path.dirname(__file__)
    folder_results=os.path.join(folder_script,"./out/")
    count_of_files=len(os.listdir(folder_results))
    new_filename=("%s.%d.png" % (filename,count_of_files))
    file_result=os.path.join(folder_script,"./out/",new_filename)
    skimage.io.imsave(file_result,image_result)
    print("Image saved to fileL%s" % (file_result))
#
#Define the custom function
#
def MyCustomParabola(x):
    amplitude=90
    radians_2_pix=math.pi/2 / 50
    theta=x*radians_2_pix
    y=math.sin(theta)*amplitude
    return y

#
#Generate X,Y values using custom function and superimpose over image 
#max_distance=max distance betwen 2 consecutive points
#
def generate_xy_from_custom_function(image_array,max_distance):
    x_start=0
    width=image_array.shape[1]
    height=image_array.shape[0]
    x_end=width
    y_origin=height/2

    delta_x=width*0.25 #an approx gap to being with
    x_last=x_start
    y_last=MyCustomParabola(x_last)+y_origin
    pts_new=list();
    while(x_last<x_end):
        gap=delta_x
        while(True):
            x_new=x_last+gap
            y_new=MyCustomParabola(x_new)+y_origin
            dsquare=(x_new-x_last)**2 + (y_new-y_last)**2
            d=dsquare**0.5
            if (d <= max_distance):
                pt_new=Point(x_new,y_new)
                pts_new.append(pt_new)
                x_last=x_new
                y_last=y_new
                break
            else:
                gap=gap*0.5 #reduce the gap and try again
                continue
    image_result=Util.superimpose_points_on_image(image_array,pts_new, 0,0,0)
    return image_result
    pass

blank_image=generate_blankimage_with_saltpepper_noise(img_width,img_height,salt_pepper_noise)
new_image=generate_xy_from_custom_function(blank_image,max_distance=max_distance_between_2_points)
filename="SineWave-W=%d.H=%d.MAXD=%d.SP=%.2f"%(img_width,img_height,max_distance_between_2_points,round(salt_pepper_noise,2))
save_image_to_disk(new_image,filename)







