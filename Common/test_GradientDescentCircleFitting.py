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
        self.assertassertTrue (p1 in helper._points)
        self.assertassertTrue (p2 in helper._points)


    def test_Skeleton(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
