import unittest
from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import RansacCircleHelper

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

if __name__ == '__main__':
    unittest.main()
