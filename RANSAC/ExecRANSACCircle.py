#
#Read the image containing the noisy 
#
import skimage
import os
import RansacCircleHelper as ransachelper
import Point as pmodel
import Util
import datetime
import sys
import CircleModel as cmodel

folder_script=os.path.dirname(__file__)
#
#Change the input file in the following line
#
filename="NoisyCircle-HandDrawn-001.png"
#"NoisyLine-Gaussian-sp-0.80.103.png" #change this
file_noisy_circle=os.path.join(folder_script,"./input/",filename)
np_image=skimage.io.imread(file_noisy_circle,as_gray=True)
ransac_threshold=40
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
lst_all_points=Util.create_points_from_numpyimage(np_image)
#
#begin RANSAC
#
helper=ransachelper.RansacCircleHelper()
helper.threshold_error=ransac_threshold
helper.threshold_inlier_count=4
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
new_points=cmodel.generate_points_from_circle(best_model)
np_superimposed=Util.superimpose_points_on_image(np_image_result,new_points,100,255,100)
#Save new image
skimage.io.imsave(file_result,np_superimposed)
print("Results saved to file:%s" % (file_result))
pass

