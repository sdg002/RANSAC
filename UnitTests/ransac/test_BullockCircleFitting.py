import unittest
from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import BullockCircleFitting
from RANSAC.Common import Util
import os
import skimage

class Test_test_BullockCircleFitting(unittest.TestCase):
    #def test_A(self):
    #    self.fail("Not implemented")

    def test_constructor(self):
        p1=Point(1,1)
        p2=Point(2,2)
        p3=Point(3,3)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)

        algo=BullockCircleFitting(expected_list)
        self.assertIsNotNone(algo)
        self.assertTrue (p1 in algo._points)
        self.assertTrue (p2 in algo._points)
        self.assertTrue (p3 in algo._points)
        self.assertEqual(len(algo._points),3)
        pass

    def test_3points_around_origin_unit_radius(self):
        p1=Point(+1,0)
        p2=Point(+0,1)
        p3=Point(-1,0)

        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)

        helper=BullockCircleFitting(expected_list)
        result:CircleModel =helper.FindBestFittingCircle()
        delta=0.01
        self.assertAlmostEquals(result.R, 1.0, delta=delta);
        self.assertAlmostEquals(result.X, 0.0, delta=delta);
        self.assertAlmostEquals(result.Y, 0.0, delta=delta);

    def test_5points_around_origin_unit_radius(self):
        p1=Point(+1,0)
        p2=Point(+0,1)
        p3=Point(-1,0)
        p4=Point(+0.707,+0.707)
        p5=Point(-0.707,+0.707)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)
        expected_list.append(p4)
        expected_list.append(p5)
        helper=BullockCircleFitting(expected_list)
        result:CircleModel =helper.FindBestFittingCircle()
        delta=0.01
        self.assertAlmostEquals(result.R, 1.0, delta=delta);
        self.assertAlmostEquals(result.X, 0.0, delta=delta);
        self.assertAlmostEquals(result.Y, 0.0, delta=delta);

if __name__ == '__main__':
    unittest.main()
