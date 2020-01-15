import Point as pt
import statistics 
import LineModel as lm
import random

class RansacHelper(object):
    """Encapsulates RANSAC logic"""
    _complete_list_of_points=list()
    def __init__ (self):
        pass
    max_iterations=0
    min_points_for_model=0
    # 'threshold_error' is the threshold distance from a line for a point to be classified as an inlier
    threshold_error:float=0

    #
    #Should be called once to set the full list of data points
    #
    def add_points(self,points:list):
        self._complete_list_of_points.extend(points)
        pass
    #
    #Get the collection of points
    #
    def get_points(self):
        return self._complete_list_of_points

    #
    #Main algorithm
    #
    def run(self) -> lm.LineModel:
        iter=0
        best_error=9999
        best_model=None
        while (iter < self.max_iterations):
            iter+=1
            random_points=self.select_random_points(self.min_points_for_model)
            temp_model=self.create_model(random_points)
            inliers=self.get_inliers_from_model(temp_model,random_points)
            if (len(inliers) < self.threshold_inlier_count):
                continue
            lst_new=list()
            lst_new.extend(random_points)
            lst_new.extend(inliers)
            better_model=self.create_model(lst_new)
            average_distance=self.compute_average_distance(better_model,lst_new)
            if (average_distance < best_error):
                best_model=temp_model
                best_error=average_distance

        return best_model
        pass

    def compute_average_distance(self,model:lm.LineModel,points:list):
        lst_distances=list()
        for pt in points:
            distance=model.compute_distance(pt)
            lst_distances.append(distance)
        mean=statistics.mean(lst_distances)
        return mean
    #
    #Get all points from master list (not used for model building) within error threshold
    #
    def get_inliers_from_model(self,model:lm.LineModel,points_old_inliers:list):
        lst_inliers=list()
        for pt in self._complete_list_of_points:
            if ((pt in points_old_inliers) == True):
                continue
            distance_from_model:float=model.compute_distance(pt)
            if (distance_from_model > self.threshold_error):
                continue
            lst_inliers.append(pt)
        return lst_inliers
    #
    #Returns the specified count of random selection of points from the full data set
    #
    def select_random_points(self,count:int):
        #Temporary implementation only
        count_original=len(self._complete_list_of_points)
        if (count >= count_original):
            message="The count of random points:%d canot exceed length of original list:%d" % (count,count_original)
            raise Exception(message)
        lst=random.choices(population=self._complete_list_of_points,k=count)
        return lst
    #
    #Find the best line which fits the specified points
    #
    def create_model(self,points):
        #temporary implementation
        model=lm.LineModel(10,20,30)
        return model
