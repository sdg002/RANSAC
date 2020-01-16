#
#Read the image containing the noisy 
#
import skimage
import os
import RansacHelper as ransachelper
import Point as pt



folder_script=os.path.dirname(__file__)
filename="Numpy.BlankImage.255.png"
file_noisy_line=os.path.join(folder_script,"./out/",filename)
np_image=skimage.io.imread(file_noisy_line,as_gray=True)
#
#Iterate over all cells of the NUMPY array and convert to array of Point classes
#
image_shape=np_image.shape
lst_all_points=list()
for x in range(0,image_shape[1]):
    for y in range(0,image_shape[0]):
        #print("x=%d y=%d" % (x,y))
        p=pt.Point(x,y)
        lst_all_points.append(p)
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
print("Found model %s" % (model))
pass

