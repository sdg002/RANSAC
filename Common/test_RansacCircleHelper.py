import unittest
import RansacCircleHelper
import math
import Point as pmodel
import CircleModel as cmodel

class Test_test_RansacCircleHelper(unittest.TestCase):

    def test_when_constructed_all_properties_must_be_intialized(self):
        helper=RansacCircleHelper.RansacCircleHelper()
        self.assertTrue(math.isnan(helper.threshold_error))
        self.assertIsNotNone(helper._all_points)

    #
    #Iterate over all points and generate all possible trigrams (combinations of 3 points) 
    #
    def test_generate_trigram_of_points_with_only3_points_in_the_universe(self):
        helper=RansacCircleHelper.RansacCircleHelper()
        universe=list()
        universe.append(pmodel.Point(0,0))
        universe.append(pmodel.Point(1,1))
        universe.append(pmodel.Point(2,2))
        helper.add_points(universe)
        trigrams=helper.generate_trigam_from_points()
        self.assertTrue(len(trigrams),1)
        tri0:RansacCircleHelper.TrigramOfPoints=trigrams[0]
        self.assertTrue(tri0.P1 in universe)
        self.assertTrue(tri0.P2 in universe)
        self.assertTrue(tri0.P3 in universe)
        pass

    def test_generate_trigam_from_points_with_only4_points_in_the_universe(self):
        helper=RansacCircleHelper.RansacCircleHelper()
        universe=list()
        universe.append(pmodel.Point(0,0))
        universe.append(pmodel.Point(1,1))
        universe.append(pmodel.Point(2,2))
        universe.append(pmodel.Point(3,3))
        helper.add_points(universe)
        trigrams=helper.generate_trigam_from_points()
        self.assertTrue(len(trigrams),4)

    def test_when_trigram_is_constructed_all_properties_must_be_initialized(self):
        p1=pmodel.Point(1,1)
        p2=pmodel.Point(2,2)
        p3=pmodel.Point(3,3)

        tri=RansacCircleHelper.TrigramOfPoints(p1,p2,p3)
        self.assertTrue(tri.P1.ID == p1.ID)
        self.assertTrue(tri.P2.ID == p2.ID)
        self.assertTrue(tri.P3.ID == p3.ID)

    #def test_compute_model_goodness_all_points_on_circumfrence(self):
    #    helper=RansacCircleHelper.RansacCircleHelper()
    #    universe=list()
    #    universe.append(pmodel.Point(+1,0))
    #    universe.append(pmodel.Point(-1,0))
    #    universe.append(pmodel.Point(0,1))
    #    helper.add_points(universe)
    #    circ=cmodel.CircleModel(0,0,1)
    #    helper.threshold_error=4
    #    t=helper.compute_model_goodness(circ)
    #    mse=t[0]
    #    inlier_count=t[1]
    #    self.assertAlmostEqual(mse,0)
    #    self.assertAlmostEqual(inlier_count,3)
    #    pass

    #def test_compute_model_goodness_3_points_on_circumfrence_1_far_away(self):
    #    helper=RansacCircleHelper.RansacCircleHelper()
    #    universe=list()
    #    universe.append(pmodel.Point(+1,0))
    #    universe.append(pmodel.Point(-1,0))
    #    universe.append(pmodel.Point(0,1))
    #    universe.append(pmodel.Point(100,100)) #far away
    #    helper.add_points(universe)
    #    circ=cmodel.CircleModel(0,0,1)
    #    helper.threshold_error=4
    #    t=helper.compute_model_goodness(circ)
    #    mse=t[0]
    #    inlier_count=t[1]
    #    self.assertAlmostEqual(mse,0)
    #    self.assertAlmostEqual(inlier_count,3)
    #    pass
    
    def test_compute_model_goodness2_all_points_on_circumfrence(self):
        helper=RansacCircleHelper.RansacCircleHelper()
        universe=list()
        universe.append(pmodel.Point(+1,0))
        universe.append(pmodel.Point(-1,0))
        universe.append(pmodel.Point(0,1))
        helper.add_points(universe)
        circ=cmodel.CircleModel(0,0,1)
        helper.threshold_error=4
        mse=helper.compute_model_goodness2(circ, universe)
        self.assertAlmostEqual(mse,0)
        pass

if __name__ == '__main__':
    unittest.main()
