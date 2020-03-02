#
#Read the image containing the noisy 
#
import skimage
import os
import RansacCircleHelper as ransachelper
import Point as pt
import Util
import datetime
import LineModel
import sys
import CircleModel

folder_script=os.path.dirname(__file__)
#
#Change the input file in the following line
#
filename="NoisyCircle-HandDrawn-001.png"
#"NoisyLine-Gaussian-sp-0.80.103.png" #change this
file_noisy_line=os.path.join(folder_script,"./input/",filename)
np_image=skimage.io.imread(file_noisy_line,as_gray=True)
ransac_threshold=sys.float_info.max #max possible error
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
lst_all_points=Util.create_points_from_numpyimage(np_image)
#
#begin RANSAC
#
helper=ransachelper.RansacCircleHelper()
helper.threshold_error=ransac_threshold
helper.add_points(lst_all_points)
model_results=helper.run() 
print("RANSAC-complete")    
print("%d models were detected" % (len(model_results)))
for model_result in model_results:
    print("Displaying RANSAC model")
    print("Center %f,%f" % (model_result))
    print("-----------------------------------")
#Display the model , you could render over the original picture
print("Found model %s , polar=%s" % (model,model.display_polar()))
#
#Generate an output image with the model line 
#
pass

