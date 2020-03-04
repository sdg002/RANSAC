import CircleModel as cmodel
import Point as pmodel
import GradientDescentCircleFitting
from typing import List, Set, Dict, Tuple, Optional
import math
import statistics as stats

class TrigramOfPoints(object):
    def __init__(self,p1:pmodel.Point, p2:pmodel.Point, p3:pmodel.Point):
        self.P1:pmodel.Point=p1
        self.P2:pmodel.Point=p2
        self.P3:pmodel.Point=p3

        self.mean_error:float=0.0
        self.inlier_count:int=0
        pass

class RansacCircleHelper(object):
    """Implements Ransac algorithm for Circle model"""
    def __init__(self):
        self._all_points:List[pmodel.Point]=list() #all points in the population
        self.threshold_error:float=float("nan")
        self.threshold_inlier_count=4 #A lower limit on inliers to shortlist a model
        pass
    #
    #Should be called once to set the full list of data points
    #
    def add_points(self,points:List[pmodel.Point]):
        self._all_points.extend(points)
        pass

    def run(self)->cmodel.CircleModel:
        pass
        if (math.isnan(self.threshold_error) == True):
            raise Exception("The threshold has not been initialized")
        #
        #generate trigrams of points - find some temporary model to hold this model
        trigrams=self.generate_trigam_from_points()
        learning_rate=0.1
        #for ever triagram find circle model
        tri:TrigramOfPoints
        lst_results=list()
        for tri in trigrams:
            try:
                temp_circle=cmodel.GenerateModelFrom3Points(tri.P1,tri.P2,tri.P3)
            except Exception as e:
                print("Could not generate Circle model. Error=%s" % (str(e)))
                continue

            inliers:List[pmodel.Point]=self.get_inliers(temp_circle,[tri.P1,tri.P2,tri.P3])
            count_inliers=len(inliers)
            if (count_inliers < self.threshold_inlier_count):
                print("Skipping because of poor inlier count=%d and this is less than threshold=%f)" % (count_inliers, self.threshold_inlier_count))
                continue
            error=self.compute_model_goodness2(temp_circle,inliers)
            result=(temp_circle,inliers,error,tri)
            lst_results.append(result)

            
        #Fit all the other points to this model and make a note of the error
        #done with all trigrams
        #Sort trigrams with lowest error
        sorted_by_mse=  sorted(lst_results, key = lambda x: x[2])
        best_model=sorted_by_mse[0][0]
        return best_model
        pass

    '''
    Iterates over all points and generates trigrams
    @param points:Collection of points on which to iterate
    '''
    #def GenerateTrigamFromPoints(self,points:List[pmodel.Point])->List[TrigramOfPoints]:
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
    def compute_model_goodness2(self,model:cmodel.CircleModel,inliers:List[pmodel.Point])->float:
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
    def compute_model_goodness(self,model:cmodel.CircleModel)->Tuple:
        #Needs correction
        raise Exception("Method needs correction")
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:pmodel.Point
        shortlist_inliners=list()
        list_mean_errors=list()
        for p in all_points:
            squared=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            distance=math.sqrt(squared)
            absolute_error=math.fabs(distance - radius)
            if (absolute_error <= threshold):
                shortlist_inliners.append(p)
            list_mean_errors.append(absolute_error)
        mean_error=stats.mean(list_mean_errors)
        result=(mean_error,len(shortlist_inliners))
        return result

    #
    #Returns all points which are within the tolerance distance from the circumfrence of the specified circle
    #Points in the exclusion list will not be considered. 
    #
    def get_inliers(self,model:cmodel.CircleModel,exclude_points:List[pmodel.Point])->List[pmodel.Point]:
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:pmodel.Point
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
