import unittest
import RansacHelper as rh
import Point as pt

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
        helper=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,0))
        lst.append(pt.Point(1,1))
        lst.append(pt.Point(2,2))
        lst.append(pt.Point(3,3))
        helper.add_points(lst)
        rnd_pts=helper.select_random_points()#rename this method
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()
