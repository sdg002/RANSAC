import unittest
import CircleModel as cmodel
import Point as pmodel

class Test_CircleModel(unittest.TestCase):
    def test_When_Constructed_All_Properties_Must_Be_Initialized(self):
        c1= cmodel.CircleModel(100.1,200.2,300.3)
        self.assertAlmostEquals(100.1,c1.X)
        self.assertAlmostEquals(200.2,c1.Y)
        self.assertAlmostEquals(300.3,c1.R)

    def test_String_Representation_Must_Have_Center_And_Radius(self):
        c1= cmodel.CircleModel(100.1,200.2,300.3)
        display=str(c1)
        self.assertTrue(display.find("X=100.1") >= 0)
        self.assertTrue(display.find("Y=200.2") >= 0)
        self.assertTrue(display.find("R=300.3") >= 0)

    #Points  (-1,0) (0,1)  (1,0)
    def test_GenerateModelFrom3pmodels_PassingThrough_1_0_And_0_1_minus1_0(self):
        p_1_0=pmodel.Point(0,1)
        p_0_0=pmodel.Point(1,0)
        p_minus1_0=pmodel.Point(-1,0)


        c1=cmodel.GenerateModelFrom3Points(p_0_0,p_1_0,p_minus1_0)
        #Assert on radius
        self.assertAlmostEquals(c1.R, 1.0,1)
        #Assert on center X,Y
        self.assertAlmostEquals(c1.X, 0.0,1)
        self.assertAlmostEquals(c1.Y, 0.0,1)


    #Points  (-1,1) (0,2)  (1,1)
    def test_GenerateModelFrom3pmodels_PassingThrough_1_1_And_0_2_minus1_1(self):
        p_1_0=pmodel.Point(1,1)
        p_0_0=pmodel.Point(0,2)
        p_minus1_0=pmodel.Point(-1,1)


        c1=cmodel.GenerateModelFrom3Points(p_0_0,p_1_0,p_minus1_0)
        #Assert on radius
        self.assertAlmostEquals(c1.R, 1.0,1)
        #Assert on center X,Y
        self.assertAlmostEquals(c1.X, 0.0,1)
        self.assertAlmostEquals(c1.Y, 1.0,1)

    def test_generate_points_from_circle_model(self):
        self.fail("Method is not yet implemented")
if __name__ == '__main__':
    unittest.main()
