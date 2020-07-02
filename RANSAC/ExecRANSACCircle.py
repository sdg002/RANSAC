#
#Read the image containing the noisy 
#
import skimage
import os
import datetime
import sys

from RANSAC.Common import Util
from RANSAC.Common import CircleModel
from RANSAC.Common import Point
from RANSAC.Algorithm import RansacCircleHelper


folder_script=os.path.dirname(__file__)
#
#Change the input file in the following line
#
filename6="NoisyCircle_x_-10_y_-14_r_48_d_0.400000_sp_0.8.186.png"
filename5="NoisyCircle_x_118_y_59_r_100_d_0.200000_sp_0.8.183.png"
filename4="NoisyCircle_x_60_y_143_r_103_d_0.400000_sp_0.8.182.png"
filename3="NoisyCircle_x_116_y_-15_r_133_d_0.500000_sp_0.5.177.png"
filename1="NoisyCircle_1.png"
filename2="NoisyCircle_2.png"
filename0="NoisyCircle-HandDrawn-001.png"

filename=filename0
file_noisy_circle=os.path.join(folder_script,"./input/",filename)
np_image=skimage.io.imread(file_noisy_circle,as_gray=True)
ransac_threshold=10 #20

#YOU WERE LOOKING AT WHY WE CHOSE A HIGHT VALUE OF 40 FOR ransac_threshold
#Are we dividing the MSE by N
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
lst_all_points=Util.create_points_from_numpyimage(np_image)
#
#begin RANSAC
#
helper=RansacCircleHelper()
helper.threshold_error=ransac_threshold
helper.threshold_inlier_count=5 #20
helper.add_points(lst_all_points)
best_model=helper.run() 
print("RANSAC-complete")    
#
#Generate an output image with the model circle overlayed on top of original image
#
now=datetime.datetime.now()
filename_result=("%s-%s.png" % (filename,now.strftime("%Y-%m-%d-%H-%M-%S")))
file_result=os.path.join(folder_script,"./out/",filename_result)
#Load input image into array
np_image_result=skimage.io.imread(file_noisy_circle,as_gray=True)
new_points=CircleModel.generate_points_from_circle(best_model)
np_superimposed=Util.superimpose_points_on_image(np_image_result,new_points,100,255,100)
#Save new image
skimage.io.imsave(file_result,np_superimposed)
print("Results saved to file:%s" % (file_result))
pass

