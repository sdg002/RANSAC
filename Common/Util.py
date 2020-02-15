
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
#Draws the specified collection of Point objects over the numpy array
#The coordinate system of the point will be transformed from Cartesian(bottom-left) to Image(top-left)
#
def superimpose_points_on_image(arr_image_input:np.ndarray, points,red:int,green:int,blue:int):
    width=arr_image_input.shape[1]
    height=arr_image_input.shape[0]
    arr_new=np.zeros([height,width,3])
    #We want to capture the original image
    for x in range(0,width):
        for y in range(0,height):
            color=arr_image_input[y][x]
            if (color > 0.5):
                arr_new[y][x][0]=255
                arr_new[y][x][1]=255
                arr_new[y][x][2]=255
    #superimpose the points onto the numpy array
    for p in points:
        x:int=int(round(p.X))
        y:int=int(round(height-p.Y-1))
        if (x<0 or x >= width ):
            continue
        if (y<0 or y >= height ):
            continue
        arr_new[y][x][0]=red
        arr_new[y][x][1]=green
        arr_new[y][x][2]=blue
    return arr_new
    pass

#
#Plots the points on the line starting from start point and leading to end point
#The points are written on to a ndarray that was originally a blank image
#The caller must take responsibility for ensuring that end coordinate values do not exceed the dimensions of the array
#
def plot_line_2darray(np_array,x_start,y_start,x_end,y_end,num_points):
    print(np_array.shape)
    print("Plotting a straight line....., ")
    xvalues = np.linspace(x_start, x_end, num_points)
    yvalues=list()
    slope=(y_end-y_start)/(x_end - x_start)
    for index in range(0,len(xvalues)):
            x=xvalues[index]
            y=slope* (x-x_start) +y_start
            print("x=%f, y=%f" % (x,y))
            yvalues.append(y)
            np_array[int(y)][int(x)][0]=0
    return np_array

