import unittest

from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import GradientDescentCircleFitting

class Test_test_GradientDescentCircleFitting(unittest.TestCase):
    def test_Constructor_With_Learning_Rate(self):
        p1=Point(1,1)
        p2=Point(2,2)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)

        expected_lrate=1.1
        helper=GradientDescentCircleFitting(None,points=expected_list,learningrate=expected_lrate)
        self.assertEqual(expected_lrate,helper._learningrate)
        self.assertEqual(len(expected_list),len(helper._points))
        self.assertTrue (p1 in helper._points)
        self.assertTrue(p2 in helper._points)

    def test_Constructor_With_Default_Learning_Rate(self):
        p1=Point(1,1)
        p2=Point(2,2)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)

        expected_lrate=0.05
        helper=GradientDescentCircleFitting(None,points=expected_list)
        self.assertEqual(expected_lrate,helper._learningrate)
        self.assertEqual(len(expected_list),len(helper._points))
        self.assertTrue (p1 in helper._points)
        self.assertTrue(p2 in helper._points)

    #
    #A very basic test with the following 3 points only. 
    #   (+1,0)
    #   (-1,0)
    #   (0,1)
    #Expected:
    #   Should produce a perfect circle with center=(0,0) and radius=1.0
    #
    def test_3points_around_origin_unit_radius(self):
        p1=Point(+1,0)
        p2=Point(+0,1)
        p3=Point(-1,0)

        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)

        helper=GradientDescentCircleFitting(None,expected_list)
        result:CircleModel =helper.FindBestFittingCircle()
        delta=0.01
        self.assertAlmostEquals(result.R, 1.0, delta=delta);
        self.assertAlmostEquals(result.X, 0.0, delta=delta);
        self.assertAlmostEquals(result.Y, 0.0, delta=delta);
        
    def test_5points_around_origin_unit_radius(self):
        self.fail("Not implemented")

    def test_When_GD_Is_Invoked_With_less_than_3_points_Exception_MustBe_Thrown(self):
        self.fail("Not implemented")

        

    def test_Skeleton(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
