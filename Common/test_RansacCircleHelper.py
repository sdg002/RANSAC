import unittest
import RansacCircleHelper
import math

class Test_test_RansacCircleHelper(unittest.TestCase):
    def test_generate_trigam_from_points(self):
        self.fail("Not implemented")
    def test_when_constructed_all_properties_must_be_intialized(self):
        helper=RansacCircleHelper.RansacCircleHelper()
        self.assertTrue(math.isnan(helper.threshold_error))
        self.assertIsNotNone(helper._all_points)

    def generate_trigram_of_points(self):
        pass

if __name__ == '__main__':
    unittest.main()
