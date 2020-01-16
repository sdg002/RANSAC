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
        self.fail("vertical lines not yet implemented")

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

if __name__ == '__main__':
    unittest.main()
