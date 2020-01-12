import numpy as np

def PlotLineOnArray(np_array,x_start,y_start,x_end,y_end,num_points):
    print(np_array.shape)
    print("Plotting a straight line....., ")
    xvalues = np.linspace(x_start, x_end, num_points)
    yvalues=list()
    slope=(y_end-y_start)/(x_end - x_start)
    for index in range(0,len(xvalues)):
            x=xvalues[index]
            y=slope*x +y_start
            print("x=%f, y=%f" % (x,y))
            yvalues.append(y)
            np_array[int(y)][int(x)][0]=0
    return np_array

