import CircleModel as cmodel
import Point as pmodel
import GradientDescentCircleFitting as gdescent
import unittest

class Test_test_GradientDescentCircleFitting(unittest.TestCase):
    def test_Constructor(self):
        p1=pmodel.Point(1,1)
        p2=pmodel.Point(2,2)
        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)

        expected_lrate=1.1
        helper=gdescent.GradientDescentCircleFitting(None,expected_lrate,expected_list)
        self.assertEqual(expected_lrate,helper._learningrate)
        self.assertTrue (p1 in helper._points)
        self.assertTrue(p2 in helper._points)


    def test_3points_around_origin_unit_radius(self):
        p1=pmodel.Point(+1,0)
        p2=pmodel.Point(+0,1)
        p3=pmodel.Point(-1,0)

        expected_list=list()
        expected_list.append(p1)
        expected_list.append(p2)
        expected_list.append(p3)

        expected_lrate=0.1
        helper=gdescent.GradientDescentCircleFitting(None,expected_lrate,expected_list)
        result:cmodel.CircleModel =helper.FindBestFittingCircle()
        self.assertAlmostEquals(result.R, 1.0);
        self.assertAlmostEquals(result.X, 0.0);
        self.assertAlmostEquals(result.Y, 0.0);
                        

    def test_Skeleton(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
