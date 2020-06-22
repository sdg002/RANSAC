from typing import List, Set, Dict, Tuple, Optional
import math
import statistics as stats

from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import GradientDescentCircleFitting 

class TrigramOfPoints(object):
    def __init__(self,p1:Point, p2:Point, p3:Point):
        self.P1:Point=p1
        self.P2:Point=p2
        self.P3:Point=p3

        #self.mean_error:float=0.0
        #self.inlier_count:int=0
        pass

class RansacCircleHelper(object):
    """Implements Ransac algorithm for Circle model"""
    def __init__(self):
        #all points in the population
        self._all_points:List[Point]=list()

        #A point will be considered an inlier of a model circle if it is 
        #within this distance from circumfrence of the model
        self.threshold_error:float=float("nan")
        
        #A lower limit on count of inliers for a model to be shortlisted
        self.threshold_inlier_count=float("nan") 
        pass
    #
    #Should be called once to set the full list of data points
    #
    def add_points(self,points:List[Point]):
        self._all_points.extend(points)
        pass

    def run(self)->CircleModel:
        pass
        if (math.isnan(self.threshold_error) == True):
            raise Exception("The property 'threshold_error' has not been initialized")

        if (math.isnan(self.threshold_inlier_count) == True):
            raise Exception("The property 'threshold_inlier_count' has not been initialized")
        #
        #generate trigrams of points - find some temporary model to hold this model
        #
        trigrams=self.generate_trigam_from_points()
        learning_rate=0.1
        #
        #for ever triagram find circle model
        #   find the circle that passes through those points
        #   Determine model goodness score
        #
        tri:TrigramOfPoints
        lst_results=list()
        for tri in trigrams:
            try:
                temp_circle=CircleModel.GenerateModelFrom3Points(tri.P1,tri.P2,tri.P3)
            except Exception as e:
                print("Could not generate Circle model. Error=%s" % (str(e)))
                continue

            inliers:List[Point]=self.get_inliers(temp_circle,[tri.P1,tri.P2,tri.P3])
            count_inliers=len(inliers)
            if (count_inliers < self.threshold_inlier_count):
                print("Skipping because of poor inlier count=%d and this is less than threshold=%f)" % (count_inliers, self.threshold_inlier_count))
                continue
            error=self.compute_model_goodness2(temp_circle,inliers)
            result=(temp_circle,inliers,error,tri)
            lst_results.append(result)            
        #
        #Sort trigrams with lowest error
        #
        sorted_by_mse=  sorted(lst_results, key = lambda x: x[2])
        lst_results_gdescent=list()
        for t in sorted_by_mse:
            model=t[0]
            inliers=t[1]
            trigram:TrigramOfPoints=t[3]
            new_points=list()
            new_points.extend(inliers)
            new_points.append(trigram.P1)
            new_points.append(trigram.P2)
            new_points.append(trigram.P3)
            new_model=self.find_model_using_gradient_descent(model,new_points)
            new_error,found_inliers=self.compute_model_goodness(new_model)
            result=(new_model,new_error)
            lst_results_gdescent.append(result)
        lst_results_gd2=sorted(lst_results,key= lambda x: x[2])
        #you were hr# fkae thre results
        #
        #TODO take every model, 
        #   expand using all inliers that were found
        #   use GD to find best circle
        #   Compute error
        #   Take best model
        #
        best_model=sorted_by_mse[0][0]
        return best_model
        pass

    '''
    Iterates over all points and generates trigrams
    @param points:Collection of points on which to iterate
    '''
    #def GenerateTrigamFromPoints(self,points:List[Point])->List[TrigramOfPoints]:
    def generate_trigam_from_points(self,):
        lst=list()
        points=self._all_points
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                for k in range(j+1,len(points)):
                    p0=points[i]
                    p1=points[j]
                    p2=points[k]
                    trigram=TrigramOfPoints(p0,p1,p2)
                    lst.append(trigram)
        return lst
        pass
    
    #
    #Compute the mean squared error of the inlier points w.r.t circle model
    #
    def compute_model_goodness2(self,model:CircleModel,inliers:List[Point])->float:
        radius=model.R
        list_errors=list()
        for p in inliers:
            squared=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            distance=math.sqrt(squared)
            absolute_error=math.fabs(distance - radius)
            list_errors.append(absolute_error)
        return stats.mean(list_errors)

    '''
    Determine how good all the points fit the given circle equatino.
        Iterate over all points
        Pick only those points which are within 'threshold'
        Compute mean squared error for these points
        Compute the total no of inliners
    Return a tuple of mse,inlier_count
    '''
    def compute_model_goodness(self,model:CircleModel)->Tuple:
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:Point
        shortlist_inliners=list()
        summation_meas_squared=0
        for p in all_points:
            squared_distance=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            distance_from_center=math.sqrt(squared_distance)
            absolute_error=math.fabs(distance_from_center - radius)
            if (absolute_error > threshold):
                #skip point if outlier
                continue
            shortlist_inliners.append(p)
            e_squared=absolute_error**2
            summation_mean_squared=summation_meas_squared+e_squared

        sqrt_summation_mean_squared=math.sqrt(summation_mean_squared)
        mse=1/2*sqrt_summation_mean_squared/len(all_points)
        result=(mse,shortlist_inliners)
        return result
        ###
        #list_mean_errors=list()
        #for p in all_points:
        #    squared=(p.X - model.X)**2 + (p.Y - model.Y)**2 
        #    distance=math.sqrt(squared)
        #    e_squared=(distance - radius)*82
        #    absolute_error=math.fabs(distance - radius)
        #    if (absolute_error <= threshold):
        #        shortlist_inliners.append(p)
        #    list_mean_errors.append(absolute_error)
        #mean_error=stats.mean(list_mean_errors)
        #result=(mean_error,len(shortlist_inliners))
        #return result

    #
    #Returns all points which are within the tolerance distance from the circumfrence of the specified circle
    #Points in the exclusion list will not be considered. 
    #
    def get_inliers(self,model:CircleModel,exclude_points:List[Point])->List[Point]:
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:Point
        shortlist_inliners=list()
        for p in all_points:
            if (p in exclude_points):
                continue
            squared=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            distance=math.sqrt(squared)
            if (distance > threshold):
                continue
            shortlist_inliners.append(p)
        return shortlist_inliners
        pass

    #
    #Use the gradience descent algorithm to find the circle that fits the givens points
    #use the modelhint as a starting circle
    #
    def find_model_using_gradient_descent(self,modelhint:CircleModel, points:List[Point])->CircleModel:
        gdhelper=GradientDescentCircleFitting.GradientDescentCircleFitting(modelhint,points, 0.1)
        new_model=gdhelper.FindBestFittingCircle()
        return new_model
        pass