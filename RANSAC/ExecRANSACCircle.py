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
def run(filename,threshold,inlier,sampling_fraction=0.25):
    print("Going to process file:%s" % (filename))
    folder_script=os.path.dirname(__file__)
    file_noisy_circle=os.path.join(folder_script,"./input/",filename)
    try:
        np_image=skimage.io.imread(file_noisy_circle,as_gray=True)

        #
        #Iterate over all cells of the NUMPY array and convert to array of Point classes
        #
        lst_all_points=Util.create_points_from_numpyimage(np_image)
        #
        #begin RANSAC
        #
        helper=RansacCircleHelper()
        helper.threshold_error=threshold
        helper.threshold_inlier_count=inlier
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
        print("------------------------------------------------------------")
    except Exception as e:
        print("Error:%s while doing RANSAC on the file: %s" % (str(e),filename))
        print("------------------------------------------------------------")
        pass



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



#run(filename0,20,5)
#run(filename3,2,30)
#run(filename4,2,30)
#run(filename5,2,20)

#run("NoisyCircle_x_16_y_35_r_20_d_0.40_sp_0.80_w_25_h_25.196.png",2,8)
#run("NoisyCircle_x_36_y_15_r_21_d_0.40_sp_0.80_w_25_h_25.198.png",2,8)
#run("NoisyCircle_x_-5_y_5_r_19_d_0.40_sp_0.80_w_25_h_25.197.png",2,8)
#run("NoisyCircle_x_-5_y_-9_r_24_d_0.40_sp_0.80_w_25_h_25.199.png",1,7)

#run("NoisyCircle_x_20_y_2_r_22_d_0.40_sp_0.80_w_25_h_25.1.png00",1,7)
#run("NoisyCircle_x_32_y_28_r_25_d_0.40_sp_0.80_w_25_h_25.0.png",1,7)

#run("NoisyCircle_x_-4_y_51_r_33_d_0.40_sp_0.90_w_50_h_50.16.png",2,15)
#run("NoisyCircle_x_36_y_-12_r_57_d_0.40_sp_0.90_w_50_h_50.15.png",2,15)
#run("NoisyCircle_x_-15_y_-7_r_58_d_0.40_sp_0.90_w_50_h_50.14.png",2,15)





