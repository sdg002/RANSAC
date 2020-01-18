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
        folder_script=os.path.dirname(__file__)
        filename="Util_unittest.png"
        file_noisy_line=os.path.join(folder_script,"./input/",filename)
        np_image=skimage.io.imread(file_noisy_line,as_gray=True)
        height=np_image.shape[0]
        width=np_image.shape[1]

        lst_points=Util.create_points_from_numpyimage(np_image)
        np_shape=np_image.shape
        self.assertEqual(len(lst_points) , np_shape[0] * np_shape[1])
        pt_pic_topleft=lst_points[0]
        self.assertEqual(pt_pic_topleft.X,0)
        self.assertEqual(pt_pic_topleft.Y,height-1)

        pt_pic_topright=lst_points[24]
        self.assertEqual(pt_pic_topright.X,width-1)
        self.assertEqual(pt_pic_topright.Y,height-1)

        pt_pic_botleft=lst_points[5]
        self.assertEqual(pt_pic_botleft.X,0)
        self.assertEqual(pt_pic_botleft.Y,0)

        pt_pic_botright=lst_points[29]
        self.assertEqual(pt_pic_botright.X,width-1)
        self.assertEqual(pt_pic_botright.Y,0)


if __name__ == '__main__':
    unittest.main()
