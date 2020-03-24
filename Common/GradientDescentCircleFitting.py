import CircleModel as cmodel
import Point as pmodel
from typing import List, Set, Dict, Tuple, Optional

class GradientDescentCircleFitting(object):
    """Finds the best fit circle using Gradient descent approach"""
    def __init__(self, modelhint:cmodel.CircleModel,learningrate:float, points:List[pmodel.Point]):
        self._modelhint=modelhint
        self._learningrate=learningrate
        self._points=points
        pass

    def FindBestFittingCircle(self)->cmodel.CircleModel:
        #you were here
        #write an unit test
        #implement this method
        raise Exception("not yet implemented")
        pass


