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

        #self.P1=p1
        #self.P2=p1
        #self.P3=p3

        self.mean_error:float=0.0
        self.inlier_count:int=0
        pass

class RansacCircleHelper(object):
    """Implements Ransac algorithm for Circle model"""
    def __init__(self):
        self._all_points:List[pmodel.Point]=list() #all points in the population
        self.threshold_error:float=float("nan")
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
        lst_trigrams=list()
        for tri in trigrams:
            try:
                model=cmodel.GenerateModelFrom3Points(tri.P1,tri.P2,tri.P3)
                model_error,inliner_count=self.compute_model_goodness(model)
                tri.inlier_count=inliner_count
                lst_trigrams.appeend(tri)
            except:
                print("Could not generate Circle model")
            
            
        #Fit all the other points to this model and make a note of the error
        #done with all trigrams
        #Sort trigrams with lowest error
        sorted_by_mse=lst_trigrams.sort()

        #you were here - continue with the break down
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
    
    '''
    Determine how good all the points fit the given circle equatino.
        Iterate over all points
        Pick only those points which are within 'threshold'
        Compute mean squared error for these points
        Compute the total no of inliners
    Return a tuple of mse,inlier_count
    '''
    def compute_model_goodness(self,model:cmodel.CircleModel)->Tuple:
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:pmodel.Point
        shortlist_inliners=list()
        list_distances=list()
        for p in all_points:
            distance=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            if (distance > threshold):
                continue
            shortlist_inliners.append(p)
            list_distances.append(distance)
        mean_squared_error=stats.mean(list_distances)
        result=(mean_squared_error,len(shortlist_inliners))
        return result
