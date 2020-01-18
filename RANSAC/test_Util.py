import unittest
import Util
import numpy as np
import os
import skimage

class Test_test_Util(unittest.TestCase):
    def test_create_points_from_numpyimage(self):
        folder_script=os.path.dirname(__file__)
        filename="Util_unittest.png"
        file_noisy_line=os.path.join(folder_script,"./input/",filename)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        lst_points=Util.create_points_from_numpyimage(np_image)
        np_shape=np_image.shape
        self.assertEqual(len(lst_points) , np_shape[0] * np_shape[1])

if __name__ == '__main__':
    unittest.main()
