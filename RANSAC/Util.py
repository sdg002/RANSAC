
import Point as pt
import numpy as np

#
#Generates a list of Point classes from 2d numpy array
#The numpy array has the origin at the top left corner
#The coordinate system will be shifted to bottom-left (Cartesian)
#Only pixels with value greater than 128 will be returned
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
            color=arr_image[y][x]
            #we want black pixels only
            if (color > 0.5):
                continue

            y_cartesian=image_ht - y -1
            p=pt.Point(x,y_cartesian)
            lst.append(p)
    return lst
#
#Draws the specified collection of points over the numpy array
#The coordinate system of the point will be transformed from Cartesian(bottom-left) to Image(top-left)
#
def superimpose_points_on_image(arr_image:np.ndarray, points,red:int,green:int,blue:int):
    width=arr_image.shape[1]
    height=arr_image.shape[0]
    arr_new=np.zeros([height,width,3])
    for p in points:
        x=p.X
        y=height-p.Y-1
        arr_new[y][x][0]=red
        arr_new[y][x][1]=green
        arr_new[y][x][2]=blue
    return arr_new
    pass
