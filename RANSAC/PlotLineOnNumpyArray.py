import numpy as np
import GenerateGaussianNoiseAtPoint as gsnoise

def PlotLineOnArray(np_array,x_start,y_start,x_end,y_end,num_points):
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

    ##Commenting out for now - we will solve RANSAC using salt-pepper noise only
    ##Generate Gaussian noise for every point on the line
    ##
    #stddev=5
    #for index in range(0,len(xvalues)):
    #        x=xvalues[index]
    #        y=yvalues[index]
    #        arr_cluster=gsnoise.GenerateClusterOfRandomPointsAroundXY(x,y,stddev,10)
    #        cluster_shape=arr_cluster.shape
    #        for idx in range(0,cluster_shape[0]):
    #            x_cluster=arr_cluster[idx][0]; 
    #            y_cluster=arr_cluster[idx][1];
    #            np_array[int(y_cluster)][int(x_cluster)][0]=0
    return np_array

