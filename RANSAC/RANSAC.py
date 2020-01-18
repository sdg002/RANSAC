#
#Read the image containing the noisy 
#
import skimage
import os
import RansacHelper as ransachelper
import Point as pt
import Util



folder_script=os.path.dirname(__file__)
filename="NoisyImage_1.png"
#filename="tiny.png"
file_noisy_line=os.path.join(folder_script,"./input/",filename)
np_image=skimage.io.imread(file_noisy_line,as_gray=True)
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
lst_all_points=Util.create_points_from_numpyimage(np_image)

#
#begin RANSAC
#
ransac_maxiterations=3000
ransac_minpoints=20
ransac_threshold=5
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

#TODO YOU WILL NEED TO RENDER THE LINE
#TODO YOU WILL NEED TO ASSESS HOW MANY POINTS ARE INLINERS
pass

