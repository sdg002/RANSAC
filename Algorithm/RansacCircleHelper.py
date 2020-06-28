from typing import List, Set, Dict, Tuple, Optional
import math
import statistics as stats
import random
from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from RANSAC.Algorithm import GradientDescentCircleFitting 
import threading

class TrigramOfPoints(object):
    def __init__(self,p1:Point, p2:Point, p3:Point):
        self.P1:Point=p1
        self.P2:Point=p2
        self.P3:Point=p3

        pass

class RansacCircleHelper(object):
    """Implements Ransac algorithm for Circle model"""
    def __init__(self):
        #all points in the population
        self._all_points:List[Point]=list()

        #A point will be considered an inlier of a model circle if it is 
        #within this distance from circumfrence of the model
        self.threshold_error:float=float("nan")
        
        #Minimum count of inliers needed for a model to be shortlisted
        self.threshold_inlier_count=float("nan") 

        #The learning rate used for Gradient descent circle fitting algorithm
        self.learning_rate=0.1

        #The algorithm will run for these many iterations
        self.max_iterations=100

        #These many points will be selected at random to build a model
        self.min_points_for_model=20
        pass
    #
    #Should be called once to set the full list of data points
    #
    def add_points(self,points:List[Point]):
        self._all_points.extend(points)
        pass

    ##
    ##Returns a List of circle model tuples in descending order of inlier count
    ##Structure of tuple:
    ##   (circle_model,inlier_count)
    ##
    #def run2(self):
    #    self.validate_hyperparams()
    #    #
    #    #generate trigrams of points - find some temporary model to hold this model
    #    #
    #    iter=0
    #    shortlist_models=[] #tuple of circle model, error
    #    while (iter < self.max_iterations):
    #        print("Iteration %d" % (iter))
    #        iter+=1
    #        random_points=self.select_random_points(self.min_points_for_model)
    #        temp_circle=self.find_model_using_gradient_descent(None,random_points)
    #        if (temp_circle==None):
    #            continue

    #        inliers:List[Point]=self.get_inliers2(temp_circle)
    #        count_of_inliers=len(inliers)
    #        #if (count_of_inliers < self.threshold_inlier_count):
    #        #    print("   Skipping because of poor inlier count (%d less than %d)" % (count_of_inliers,self.threshold_inlier_count))
    #        #    continue
    #        t=(temp_circle,random_points,inliers)
    #        shortlist_models.append(t)
    #    sorted_shortlist_models=sorted(shortlist_models, key = lambda x: len(x[2]), reverse=True)

    #    #you were hre - you got the first short list
    #    count_of_shorlist=len(sorted_shortlist_models)
    #    second_shortlist=[]
    #    for index in range(0,count_of_shorlist):
    #        model=sorted_shortlist_models[index][0]
    #        random_points=set(sorted_shortlist_models[index][1])
    #        inliers=set(sorted_shortlist_models[index][2])
    #        also_inliers=random_points.union(inliers)
    #        temp_circle=self.find_model_using_gradient_descent(model,list(also_inliers))
    #        if (temp_circle==None):
    #            continue
    #        new_error,new_inliers=self.compute_model_goodness(temp_circle)
    #        if (len(new_inliers) < self.threshold_inlier_count):
    #            print("Skipping candidate because of low inlier count %d " % (new_inliers))
    #            continue;
    #        result=(temp_circle,new_error,new_inliers)
    #        second_shortlist.append(result)


    #    #run thorugh the short list
    #    #expand the inliners from the tuple and re-build model
    #    #for every new model, compute average distance -- take inspiration from line
    #    sorted_second_shortlist=sorted(second_shortlist, key = lambda x: (len(x[2])), reverse=True)
    #    if (len(sorted_second_shortlist) == 0):
    #        return None
    #    return sorted_second_shortlist[0][0]
        
    #    pass

        

    def validate_hyperparams(self):
        if (math.isnan(self.threshold_error) == True):
            raise Exception("The property 'threshold_error' has not been initialized")

        if (math.isnan(self.threshold_inlier_count) == True):
            raise Exception("The property 'threshold_inlier_count' has not been initialized")

        if (math.isnan(self.learning_rate) == True):
            raise Exception("The property 'threshold_inlier_count' has not been initialized")

    def run(self)->CircleModel:
        self.validate_hyperparams()

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
        lst_trigram_scores=list()
        for trig_index in range(0,len(trigrams)):
            tri=trigrams[trig_index]
            if (trig_index%100 ==0):
                print("Processing trigram %d of %d" % (trig_index,len(trigrams)))
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
            result=(temp_circle,inliers,tri)

            lst_trigram_scores.append(result)            
        #
        #Sort trigrams with lowest error
        #
        sorted_trigram_inliercount=sorted(lst_trigram_scores, key = lambda x: len(x[1]),reverse=True)
        
        lst_results_gdescent=list()
        jobs=[]
        for index in range(0,len(sorted_trigram_inliercount)):
            t=sorted_trigram_inliercount[index]
            model=t[0]
            inliers=t[1]
            trigram:TrigramOfPoints=t[2]
            new_points=list()
            new_points.extend(inliers)
            new_points.append(trigram.P1)
            new_points.append(trigram.P2)
            new_points.append(trigram.P3)
            new_thread=threading.Thread(target=self.find_model_using_gradient_descent2,args=(model,new_points,lst_results_gdescent))
            jobs.append(new_thread)

        for j in jobs:
            j.start();

        #Wait for all threads to finish!
        for j in jobs:
            j.join();        
        
        lst_results_gd2=sorted(lst_results_gdescent,key= lambda x: len(x[1]),reverse=True)
        if (len(lst_results_gd2) == 0):
            return None
        best_model=lst_results_gd2[0][0]
        return best_model

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
            distance_from_center=math.sqrt(squared)
            distance_from_circumfrence=math.fabs(distance_from_center - model.R)
            if (distance_from_circumfrence > threshold):
                continue
            shortlist_inliners.append(p)
        return shortlist_inliners
        pass

    #
    #Iterates over all points in the population and finds points 
    #which are within the allowable threshold
    #
    def get_inliers2(self,model:CircleModel)->List[Point]:
        radius=model.R
        all_points=self._all_points
        threshold=self.threshold_error
        p:Point
        shortlist_inliners=list()
        for p in all_points:
            squared=(p.X - model.X)**2 + (p.Y - model.Y)**2 
            distance_from_center=math.sqrt(squared)
            distance_from_circumfrence=math.fabs(distance_from_center - model.R)
            if (distance_from_circumfrence > threshold):
                continue
            shortlist_inliners.append(p)
        return shortlist_inliners
        pass


    #
    #Use the gradience descent algorithm to find the circle that fits the givens points
    #use the modelhint as a starting circle
    #
    def find_model_using_gradient_descent(self,modelhint:CircleModel, points:List[Point])->CircleModel:
        try:
            gdhelper=GradientDescentCircleFitting.GradientDescentCircleFitting(modelhint,points, learningrate= self.learning_rate, iterations=2000)
            new_model=gdhelper.FindBestFittingCircle()
            return new_model
        except Exception as e:
            print("Error while Gradient descent: %s" % (str(e)))
            return None
        pass

    #
    #This method was written with the expectation that it would be called in the context of a new thread
    #
    def find_model_using_gradient_descent2(self,modelhint:CircleModel, points:List[Point],lst_results):
        new_model=None
        try:
            gdhelper=GradientDescentCircleFitting.GradientDescentCircleFitting(modelhint,points, learningrate= self.learning_rate, iterations=2000)
            new_model=gdhelper.FindBestFittingCircle()
        except Exception as e:
            #print("Error while Gradient descent: %s" % (str(e)))
            pass
        if (new_model == None):
            return
        new_inliers=self.get_inliers2(new_model)
        if (len(new_inliers) == 0):
            return
        result=(new_model,new_inliers)
        lst_results.append(result)
        return
    #
    #Returns the specified count of random selection of points from the full data set
    #
    def select_random_points(self,count:int):
        count_original=len(self._all_points)
        if (count >= count_original):
            message="The count of random points:%d canot exceed length of original list:%d" % (count,count_original)
            raise Exception(message)
        lst=random.sample(population=self._all_points,k=count)
        return lst
