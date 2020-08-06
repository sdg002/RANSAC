import numpy as np
import os
import skimage
import random
import math
from RANSAC.Common import Point
from RANSAC.Common import Util

class GenericCurveGenerator(object):
    """Generic class that abtracts the drawing of a noisy curve on a canvas of given width and height"""
    def __init__ (self,width,height):
        self._width=width
        self._height=height
        self._saltpepper=0.9
        self._img_back_color=255
        self._output_file=None
        self._max_distance_consecutive_points=10
        pass
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height=value

    @property
    def saltpepper(self):
        return self._saltpepper

    @saltpepper.setter
    def saltpepper(self,value):
        self._saltpepper=value

    @property
    def output_file(self):
        return self._output_file

    @output_file.setter
    def output_file(self,value):
        self._output_file=value
    
    @property
    def max_consecutive_distance(self):
        return self._max_distance_consecutive_points

    @max_consecutive_distance.setter
    def max_consecutive_distance(self,value):
        self._max_distance_consecutive_points=value

    def __generate_blankimage_with_saltpepper_noise(self):
        #width,height,saltpepper_noise
        img = np.zeros([self.height,self.width,1],dtype=np.uint8)
        img.fill(self._img_back_color)
        image_noisy=skimage.util.random_noise(img,mode="s&p",seed=None, clip=True,salt_vs_pepper=self.saltpepper)
        return image_noisy

    #
    #Generate X,Y values using custom function and superimpose over image 
    #max_distance=max distance betwen 2 consecutive points
    #
    def __generate_xy_from_custom_function(self,image_array):
        max_distance=self._max_distance_consecutive_points
        x_start=0
        width=image_array.shape[1]
        height=image_array.shape[0]
        x_end=width
        y_origin=height/2

        delta_x=width*0.25 #an approx gap to being with
        x_last=x_start
        y_last=self.__SineFunction(x_last ,width=width,height=height)+y_origin
        pts_new=list();
        while(x_last<x_end):
            gap=delta_x
            while(True):
                x_new=x_last+gap
                y_new=self.__SineFunction(x_new,width=width,height=height)+y_origin
                dsquare=(x_new-x_last)**2 + (y_new-y_last)**2
                d=dsquare**0.5
                if (d <= max_distance):
                    pt_new=Point(x_new,y_new)
                    pts_new.append(pt_new)
                    x_last=x_new
                    y_last=y_new
                    break
                else:
                    gap=gap*0.5 #reduce the gap and try again
                    continue
        image_result=Util.superimpose_points_on_image(image_array,pts_new, 0,0,0)
        return image_result
        pass

    def __SineFunction(self,x, width,height):
        amplitude=height*0.5*0.9
        radians_to_pix=math.pi/2 / (height*0.25)
        theta=x*radians_to_pix
        y=math.sin(theta)*amplitude
        return y

    def generate_curve(self):
        blank_image=self.__generate_blankimage_with_saltpepper_noise()
        new_image=self.__generate_xy_from_custom_function(blank_image)
        self.__save_image_to_disk(new_image,self.output_file)
        pass

    #
    #Generates a filename derived from the properties of the class
    #Rationale - a simple way to visually trace back what was used
    #
    def generate_filename_prefix(self):
        sp_ratio=round(self.saltpepper,2)
        filename="W=%d.H=%d.MAXD=%d.SP=%.2f"%(self.width,self.height,self.max_consecutive_distance,sp_ratio)
        return filename

    def __save_image_to_disk(self,image_array,filename):
        image_result=image_array
        folder_script=os.path.dirname(__file__)
        folder_results=os.path.join(folder_script,"./out/")
        count_of_files=len(os.listdir(folder_results))
        new_filename=("%s.%d.png" % (filename,count_of_files))
        file_result=os.path.join(folder_script,"./out/",new_filename)
        skimage.io.imsave(file_result,image_result)
        print("Image saved to fileL%s" % (file_result))
    