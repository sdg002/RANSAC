from RANSAC.Common import Point
from RANSAC.Common import CircleModel

from typing import List, Set, Dict, Tuple, Optional

class GradientDescentCircleFitting(object):
    """Finds the best fit circle using Gradient descent approach"""
    def __init__(self, modelhint:CircleModel,learningrate:float, points:List[Point]):
        self._modelhint=modelhint
        self._learningrate=learningrate
        self._points=points
        pass

    def FindBestFittingCircle(self)->CircleModel:
        #you were here
        #write an unit test
        #implement this method
        raise Exception("not yet implemented")
        pass


