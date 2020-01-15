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
        helper1=rh.RansacHelper()
        lst=list()
        lst.append(pt.Point(0,0))
        lst.append(pt.Point(1,1))
        lst.append(pt.Point(2,2))
        lst.append(pt.Point(3,3))
        helper1.add_points(lst)
        rnd_pts=helper1.select_random_points(2)
        self.assertEquals(len(rnd_pts), 2)
        for rnd_pt in rnd_pts:
            is_member=(rnd_pt in lst)
            print("ID of random pt=%d" % rnd_pt.ID)
            self.assertEqual(is_member,True)

if __name__ == '__main__':
    unittest.main()
