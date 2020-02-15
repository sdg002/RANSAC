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
        distance_actual=x.compute_distance(test_origin)
        distance_expected=0
        self.assertEqual(distance_actual,distance_expected)
        pass

    def test_distance_of_1_0_from_slope_45degrees_yintercept_is_zero(self):
        x=lm.LineModel(-1,1,0)
        test_point=pt.Point(1,0)
        distance_actual=x.compute_distance(test_point)
        distance_expected=1/math.sqrt(2)
        self.assertEqual(distance_actual,distance_expected)
        pass

    def test_distance_of_0_0_from_flat_line_yintercept_is_zero(self):
        x=lm.LineModel(0,1,-3)
        test_point=pt.Point(0,0)
        distance_actual=x.compute_distance(test_point)
        distance_expected=3
        self.assertEqual(distance_actual,distance_expected)
        pass

    def test_x_y_intercept_45_degrees_0_0(self):
        line=lm.LineModel(-1,1,0)
        xintercept_actual=line.xintercept()
        xintercept_expected=0
        yintercept_actual=line.yintercept()
        yintercept_expected=0

        self.assertEqual(xintercept_actual,xintercept_expected)
        self.assertEqual(yintercept_actual,yintercept_expected)

    def test_x_y_intercept_45_degrees_1_0(self):
        line=lm.LineModel(-1,1,1)
        xintercept_actual=line.xintercept()
        xintercept_expected=1
        yintercept_actual=line.yintercept()
        yintercept_expected=-1

        self.assertEqual(xintercept_actual,xintercept_expected)
        self.assertEqual(yintercept_actual,yintercept_expected)

    def test_x_y_intercept_90_degrees_5_inf(self):
        line=lm.LineModel(1,0,-5)
        xintercept_actual=line.xintercept()
        xintercept_expected=5
        yintercept_actual=line.yintercept()
        yintercept_expected=math.inf

        self.assertEqual(xintercept_actual,xintercept_expected)
        self.assertEqual(yintercept_actual,yintercept_expected)

    def test_x_y_intercept_0_degrees_inf_5(self):
        line=lm.LineModel(0,1,-5)
        xintercept_actual=line.xintercept()
        xintercept_expected=math.inf
        yintercept_actual=line.yintercept()
        yintercept_expected=5

        self.assertEqual(xintercept_actual,xintercept_expected)
        self.assertEqual(yintercept_actual,yintercept_expected)

    def test_display_polar(self):
        line=lm.LineModel(-1,1,1)
        s=line.display_polar()
        print(s)

    def test_generate_points_from_line_45_degrees_passing_through_0_0(self):
        line=lm.LineModel(-1,1,0)
        x1=20
        x2=40
        y1=10
        y2=30
        new_points=lm.generate_points_from_line(line,x1,y1,x2,y2)
        for p in new_points:
            print("Testing point=%s" % (p))
            self.assertTrue(p.X >= x1)
            self.assertTrue(p.X <= x2)
            #self.assertTrue(p.Y >= y1)
            #self.assertTrue(p.Y <= y2)

    #
    #In this test we are testing a vertical line. 
    #
    def test_generate_points_from_line_90_degrees_passing_through_5_0(self):
        line=lm.LineModel(1,0,-5)
        x1=20
        x2=40
        y1=10
        y2=30
        new_points=lm.generate_points_from_line(line,x1,y1,x2,y2)
        for p in new_points:
            print("Testing point=%s" % (p))
            self.assertTrue(p.Y >= y1)
            self.assertTrue(p.Y <= y2)
    #
    #Testing function create_line_from_start_and_end for a horizontal line
    #
    def test_create_line_from_start_and_end_horizontal_line(self):
        self.fail("not yet implemented")
    #
    #create_line_from_2points - vertical line
    #
    def test_create_line_from_start_and_end_vertical_line(self):
        start_x=1
        start_y=5
        end_x=1
        end_y=25
        model=lm.create_line_from_2points(start_x,start_y,end_x,end_y)
        expected_B=0
        expected_x_intercept=start_x
        self.assertAlmostEqual(model.B,0)
        self.assertAlmostEqual(model.C/model.A,-expected_x_intercept)
    #
    #create_line_from_2points  - horizontal line
    #
    def test_create_line_from_start_and_end_horizontal_line(self):
        start_x=1
        start_y=5
        end_x=10
        end_y=5
        model=lm.create_line_from_2points(start_x,start_y,end_x,end_y)
        #equation ax+by+c=0
        #slope=-a/b
        #yinter=-c/b
        expected_A=0
        expected_y_intercept=5
        self.assertAlmostEqual(model.A,0)
        self.assertAlmostEqual(model.C/model.B,-expected_y_intercept)
    #
    #create_line_from_2points  -  slop=1,yintercept=1
    #
    def test_create_line_from_start_and_end_horizontal_line(self):
        start_x=0
        start_y=1
        end_x=1
        end_y=2
        model=lm.create_line_from_2points(start_x,start_y,end_x,end_y)
        #equation ax+by+c=0
        #slope=-a/b
        #yinter=-c/b
        expected_slope=1
        expected_y_intercept=1
        self.assertAlmostEqual(model.A/model.B, -expected_slope)
        self.assertAlmostEqual(model.C/model.B,-expected_y_intercept)
    #
    #generate_points_at_regular_intervals_stline  (0,1) to (1,2)
    #
    def test_generate_points_at_regular_intervals_stline(self):
        start_x=0
        start_y=1
        end_x=10
        end_y=11
        model=lm.create_line_from_2points(start_x,start_y,end_x,end_y)
        slope=-model.A/model.B
        yintercept=-model.C/model.B
        gap=5
        new_points=lm.generate_points_at_regular_intervals_stline(start_x,start_y,end_x,end_y,gap)
        count_of_new_points=len(new_points)
        self.assertTrue(count_of_new_points > 0)
        self.assertTrue(count_of_new_points < 4)
        for new_point in new_points:
            new_x=new_point.X
            new_y=new_point.Y
            expected_y=slope*new_x + yintercept
            self.assertAlmostEqual(new_y,expected_y)
if __name__ == '__main__':
    unittest.main()
