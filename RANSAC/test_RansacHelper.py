import unittest
import RansacHelper as rh
import Point as pt
import math
import os
import skimage
import Util

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

    def test_run_with_very_simple_image(self):
        #get a list of points
        folder_script=os.path.dirname(__file__)
        filename="Ransac_UnitTest.png"
        file_noisy_line=os.path.join(folder_script,"./input/",filename)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        lst_points=Util.create_points_from_numpyimage(np_image)

        #initialize RansalHelper
        helper1=rh.RansacHelper()
        helper1.add_points(lst_points)
        helper1.max_iterations=30
        helper1.min_points_for_model=4
        helper1.threshold_error=10
        helper1.threshold_inlier_count=3
        result_model=helper1.run()
        x_intercept=result_model.xintercept()
        y_intercept=result_model.yintercept()
        self.assertTrue ( x_intercept > 30)
        self.assertTrue ( x_intercept < 50)

        self.assertTrue ( y_intercept > 20)
        self.assertTrue ( y_intercept < 35)


        #invoke the run method



if __name__ == '__main__':
    unittest.main()
