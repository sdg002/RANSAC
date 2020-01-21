import unittest
import RansacHelper as rh
import Point as pt
import math
import os
import skimage
import Util
import LineModel

class Test_test_1(unittest.TestCase):
    def test_AddPoints(self):
        helper=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,0))
        lst.append(pt.Point(1,1))
        lst.append(pt.Point(2,2))
        lst.append(pt.Point(3,3))
        helper.add_points(lst)
        expected_count=len(lst)
        actual_count=len(helper.get_points())
        self.assertEqual(expected_count,actual_count)
        pass

    def test_GetRandomPoints(self):
        helper1=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,0))
        lst.append(pt.Point(1,1))
        lst.append(pt.Point(2,2))
        lst.append(pt.Point(3,3))
        print("displaying orignal points")
        print("------------")
        for p in lst:
            print(p)
        print("------------")
        helper1.add_points(lst)
        print("displaying points after adding to collection")
        print("------------")
        for p in helper1.get_points():
            print(p)
        print("------------")
        
        rnd_pts=helper1.select_random_points(2)
        self.assertEquals(len(rnd_pts), 2)
        for rnd_pt in rnd_pts:
            is_member=(rnd_pt in lst)
            print("ID of random pt=%d" % rnd_pt.ID)
            self.assertEqual(is_member,True)

    def test_create_model_vertical_through_x_equal_5(self):
        pass
        helper1=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(5,0))
        lst.append(pt.Point(5,1))
        lst.append(pt.Point(5,2))
        model=helper1.create_model(lst)
        expected_xintercept=5
        actual_xintercept=-model.C/model.A
        self.assertAlmostEqual(actual_xintercept,expected_xintercept)

        self.assertAlmostEqual(model.B,0)

    def test_create_model_horizontal_through_y_equal_5(self):
        pass
        helper1=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,5))
        lst.append(pt.Point(1,5))
        lst.append(pt.Point(2,5))
        model=helper1.create_model(lst)
        #y=5
        #0x+1y-5=0
        expected_slope=0.0
        actual_slope=-model.A/model.B
        actual_yintercept=-model.C/model.B
        expected_yintercept=5
        self.assertAlmostEqual(actual_slope,expected_slope)
        self.assertAlmostEqual(actual_yintercept,expected_yintercept)

    def test_create_model_45_degrees_through_origin(self):
        pass
        helper1=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,0))
        lst.append(pt.Point(1,1))
        lst.append(pt.Point(2,2))
        model=helper1.create_model(lst)
        #
        #y=x
        #-x+y+0=0
        expected_slope=1.0
        actual_slope=-model.A/model.B
        actual_yintercept=-model.C/model.B
        expected_yintercept=0
        self.assertAlmostEqual(actual_slope,expected_slope)
        self.assertAlmostEqual(actual_yintercept,expected_yintercept)

    #
    #In this test we are doing the full Ransac algorithm run on a very simple image
    #
    def test_run_with_very_simple_image(self):
        #
        #get a list of points
        #
        folder_script=os.path.dirname(__file__)
        filename_input="Ransac_UnitTest.png"
        file_noisy_line=os.path.join(folder_script,"./input/",filename_input)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        lst_points=Util.create_points_from_numpyimage(np_image)
        #
        #initialize RansalHelper
        #
        helper1=rh.RansacHelper()
        helper1.add_points(lst_points)
        helper1.max_iterations=1000
        #10000 did not work
        helper1.min_points_for_model=2
        helper1.threshold_error=3 #10
        helper1.threshold_inlier_count=3
        result_model=helper1.run()
        print("RANSAC-complete")    
        print("Found model %s , polar=%s" % (result_model,result_model.display_polar()))
        #
        #Superimpose the new line over the image
        #
        folder_results=os.path.join(folder_script,"./out/")
        count_of_files=len(os.listdir(folder_results))
        filename_results=("Ransac_UnitTest.Run.%d.png" % (count_of_files) )
        file_result=os.path.join(folder_results,filename_results)
        x_lower=0
        x_upper=np_image.shape[1]-1
        y_lower=0
        y_upper=np_image.shape[0]-1
        new_points=LineModel.generate_points_from_line(result_model,x_lower,y_lower,x_upper,y_upper)
        np_superimposed=Util.superimpose_points_on_image(np_image,new_points,100,255,100)
        skimage.io.imsave(file_result,np_superimposed)
        #
        #Asserts!
        #
        x_intercept=result_model.xintercept()
        y_intercept=result_model.yintercept()
        self.assertTrue ( x_intercept > 30,"X intercept below threshold")
        self.assertTrue ( x_intercept < 50,"X intercept above threshold")
        self.assertTrue ( y_intercept > 30,"Y intercept above threshold")
        self.assertTrue ( y_intercept < 45,"Y intercept below threshold")


if __name__ == '__main__':
    unittest.main()
