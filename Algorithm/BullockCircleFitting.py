from RANSAC.Common import Point
from RANSAC.Common import CircleModel
from typing import List, Set, Dict, Tuple, Optional

class BullockCircleFitting(object):
    """Implements Randy Bullock algorithm for circle fitting"""
    def __init__(self,points:List[Point]):
        self._points=points

    def FindBestFittingCircle(self)->CircleModel:
        pass
