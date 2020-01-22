#
#Read the image containing the noisy 
#
import skimage
import os
import RansacHelper as ransachelper
import Point as pt
import Util
import datetime
import LineModel



folder_script=os.path.dirname(__file__)
filename="NoisyImage_3.png"
#TODO NoisyImage_3.png is not generating correct results
file_noisy_line=os.path.join(folder_script,"./input/",filename)
np_image=skimage.io.imread(file_noisy_line,as_gray=True)
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
lst_all_points=Util.create_points_from_numpyimage(np_image)

#
#begin RANSAC
#
ransac_maxiterations=12000
#6000 
#12000 worked well
ransac_minpoints=5
#5 worked well
#2 gave very bad results
#20 worked well
ransac_threshold=3
#5 produced too much deviation

ransac_mininliers=10

helper=ransachelper.RansacHelper()
helper.max_iterations=ransac_maxiterations
helper.min_points_for_model=ransac_minpoints
helper.threshold_error=ransac_threshold
helper.threshold_inlier_count=ransac_mininliers
helper.add_points(lst_all_points)
model=helper.run()

#Display the model , you could render over the original picture
print("-------------------------------------")
print("RANSAC-complete")    
print("Found model %s , polar=%s" % (model,model.display_polar()))
#
#Generate an output image with the model line 
#
now=datetime.datetime.now()
filename_result=("result-%s.png") % now.strftime("%Y-%m-%d-%H-%M-%S")
file_result=os.path.join(folder_script,"./out/",filename_result)
#Load input image into array
np_image_result=skimage.io.imread(file_noisy_line,as_gray=False)
new_points=LineModel.generate_points_from_line(model,0,0,np_image_result.shape[1]-1,np_image_result.shape[0]-1)
np_superimposed=Util.superimpose_points_on_image(np_image_result,new_points,100,255,100)
#Save new image
skimage.io.imsave(file_result,np_superimposed)

#TODO YOU WILL NEED TO ASSESS HOW MANY POINTS ARE INLINERS
pass

