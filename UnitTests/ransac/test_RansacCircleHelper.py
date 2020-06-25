import unittest
from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import RansacCircleHelper
import os
import skimage
from RANSAC.Common import Util

class Test_test_RansacCircleHelper(unittest.TestCase):

    def test_When_compute_model_goodness_And_All_Points_On_Circle_Then_Error_ShouldBe_Zero(self):
        #Circle at 0,0 with unit radius
        p1=Point(+1,0)
        p2=Point(+0,1)
        p3=Point(-1,0)
        list_of_points=list()
        list_of_points.append(p1)
        list_of_points.append(p2)
        list_of_points.append(p3)

        model=CircleModel(0,0,1)
        helper=RansacCircleHelper()
        helper.threshold_error=0.2
        helper.add_points(list_of_points)
        mse,inliers=helper.compute_model_goodness(model)

        delta=0.01
        self.assertAlmostEquals(mse, 0.0, delta=delta);
        self.assertEquals(len(inliers),3)
        self.assertTrue(p1 in inliers)
        self.assertTrue(p2 in inliers)
        self.assertTrue(p3 in inliers)

    def test_When_compute_model_goodness_And_3_Points_On_Circle_And_1_Point_VeryFarAway_Then_Error_ShouldBe_Zero(self):
        #Circle at 0,0 with unit radius
        p1=Point(+1,0)
        p2=Point(+0,1)
        p3=Point(-1,0)
        pfar_away=Point(-100,100)
        list_of_points=list()
        list_of_points.append(p1)
        list_of_points.append(p2)
        list_of_points.append(p3)
        list_of_points.append(pfar_away)

        model=CircleModel(0,0,1)
        helper=RansacCircleHelper()
        helper.threshold_error=0.2
        helper.add_points(list_of_points)
        mse,inliers=helper.compute_model_goodness(model)

        delta=0.01
        self.assertAlmostEquals(mse, 0.0, delta=delta);
        self.assertEquals(len(inliers),3)
        self.assertTrue(p1 in inliers)
        self.assertTrue(p2 in inliers)
        self.assertTrue(p3 in inliers)

    def test_When_run_method_is_invoked_on_hand_drawn_points_then_circle_must_be_found(self):
        #
        #get a list of points
        #
        folder_script=os.path.dirname(__file__)
        filename_input="NoisyCircle-HandDrawn-001.png"
        file_noisy_line=os.path.join(folder_script,"./data/",filename_input)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        lst_points=Util.create_points_from_numpyimage(np_image)
        #
        #initialize RansalHelper
        #
        ransac_threshold=40
        helper=RansacCircleHelper()
        helper.threshold_error=ransac_threshold
        helper.threshold_inlier_count=4
        helper.add_points(lst_points)
        best_model=helper.run() 
        #
        #Superimpose the new line over the image
        #
        folder_results=os.path.join(folder_script,"../out/")
        count_of_files=len(os.listdir(folder_results))
        filename_results=("%s.%d.png" % (__name__,count_of_files) )
        file_result=os.path.join(folder_results,filename_results)
        new_points=CircleModel.generate_points_from_circle(best_model)
        np_superimposed=Util.superimpose_points_on_image(np_image,new_points,100,255,100)
        skimage.io.imsave(file_result,np_superimposed)
        #
        #Assertions
        #
        self.assertAlmostEqual(best_model.X,75.8,delta=0.1)
        self.assertAlmostEqual(best_model.Y,77.7,delta=0.1)
        self.assertAlmostEqual(best_model.R,36.09,delta=0.1)

        pass

if __name__ == '__main__':
    unittest.main()
