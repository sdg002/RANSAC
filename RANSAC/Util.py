
import Point as pt
import numpy as np

#
#Generates a list of Point classes from 2d numpy array
#The numpy array has the origin at the top left corner
#The coordinate system will be shifted to bottom-left (Cartesian)
#
def create_points_from_numpyimage(arr_image:np.ndarray):
    pass
    lst=list()
    image_shape=arr_image.shape
    image_ht=image_shape[0]
    image_width=image_shape[1]
    for x in range(0,image_width):
        for y in range(0,image_ht):
            #print("x=%d y=%d" % (x,y))
            #Change coordinate system
            y_cartesian=image_ht - y -1
            p=pt.Point(x,y_cartesian)
            lst.append(p)
    return lst