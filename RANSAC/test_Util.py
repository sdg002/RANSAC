import unittest
import Util
import numpy as np
import os
import skimage

class Test_test_Util(unittest.TestCase):
    #
    #Use a simple image to test the loading of points
    #
    def test_create_points_from_numpyimage(self):
        pass
        folder_script=os.path.dirname(__file__)
        filename="Util_unittest.png"
        file_noisy_line=os.path.join(folder_script,"./input/",filename)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        height=np_image.shape[0]
        width=np_image.shape[1]

        lst_points=Util.create_points_from_numpyimage(np_image)
        np_shape=np_image.shape
        self.assertEqual(len(lst_points) , 3)

        for pt_any in lst_points:
            if pt_any.X == 0 and pt_any.Y == height-1:
                pass
            elif (pt_any.X == width-1 and pt_any.Y == height-1):
                pass
            elif (pt_any.X == width-1 and pt_any.Y == 0):
                pass
            else:
               raise Exception("Point '%s' was not expected." % (pt_any))


if __name__ == '__main__':
    unittest.main()
