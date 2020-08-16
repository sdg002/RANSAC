import numpy as np
from typing import Dict, List
from RANSAC.Common import LineModel
from RANSAC.Algorithm import RansacLineHelper
from RANSAC.Common import Util
from RANSAC.Common import Point
from RANSAC.Common import PatchInfo,PatchResults
from .ImagePatchExtractor import ImagePatchExtractor

class PatchRansacHelper(object):
    """description of class"""
    def __init__(self):
        self._image:np.ndarray=None
        self._cropdimension=10 #the size of the patch square
        self._dict_patchregions:Dict=dict()
        self._stride=5 #the number of pixels to advance the patch window
        pass
    
    @property
    def image(self):
        return self._image

    def run(self,image):
        self._image=image
        xtractor=ImagePatchExtractor(self.image,self._cropdimension,self._stride);
        patch_results:PatchResults=xtractor.extract_patches();
        patchcount_x=patch_results.patch_indices.shape[1]
        patchcount_y=patch_results.patch_indices.shape[0]
        for x in range(0,patchcount_x):
            for y in range(0,patchcount_y):
                patchinfo:PatchInfo=patch_results.get_patch_xy(x,y)
                img_patchregion=patchinfo.image
                line=self.find_line_using_ransac(img_patchregion)
                pass
            pass
        pass

    #
    #
    #

    def find_line_using_ransac(self,np_patchregion:np.ndarray):
        lst_all_points=Util.create_points_from_numpyimage(np_patchregion)
        count_of_points_in_patch=len(lst_all_points)
        

        #create thresholds for RANSAC
        ransac_threshold_distance=(self._cropdimension)*1/5 #should be adaptive
        ransac_mininliers=0.1 * count_of_points_in_patch #automatically try out various inliers

        helper=RansacLineHelper()
        helper.max_iterations=(count_of_points_in_patch)*(count_of_points_in_patch-1)/2
        helper.min_points_for_model=2
        helper.threshold_error=ransac_threshold_distance
        helper.threshold_inlier_count=ransac_mininliers
        helper.add_points(lst_all_points)
        model=helper.run()
        return model 
        pass

