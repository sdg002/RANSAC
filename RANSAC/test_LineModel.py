import unittest
import LineModel as lm
import Point as pt
import math
class Test_LineModel(unittest.TestCase):
    def test_construction(self):
        x=lm.LineModel(100,200,300)
        self.assertEqual(x.A,100)
        self.assertEqual(x.B,200)
        self.assertEqual(x.C,300)
        pass

    def test_distance_of_origin_from_slope_45degrees_yintercept_is_zero(self):
        x=lm.LineModel(-1,1,0)
        test_origin=pt.Point(0,0)
        distance_actual=x.get_distance(test_origin)
        distance_expected=0
        self.assertEqual(distance_actual,distance_expected)
        pass

    def test_distance_of_1_0_from_slope_45degrees_yintercept_is_zero(self):
        x=lm.LineModel(-1,1,0)
        test_point=pt.Point(1,0)
        distance_actual=x.get_distance(test_point)
        distance_expected=1/math.sqrt(2)
        self.assertEqual(distance_actual,distance_expected)
        pass

    def test_distance_of_0_0_from_flat_line_yintercept_is_zero(self):
        x=lm.LineModel(0,1,-3)
        test_point=pt.Point(0,0)
        distance_actual=x.get_distance(test_point)
        distance_expected=3
        self.assertEqual(distance_actual,distance_expected)
        pass

if __name__ == '__main__':
    unittest.main()
