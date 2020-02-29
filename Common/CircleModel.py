import Point as pmodel

class CircleModel(object):
    """Represents a Circle model using its center point and radius"""
    def __init__(self, center_x:float,center_y:float,radius:float):
        self.X:float=center_x
        self.Y:float=center_y
        self.R:float=radius
        pass

    def __str__(self):
        display=("X=%f Y=%f R=%f" % (self.X,self.Y,self.R))
        return display
    
def GenerateModelFrom3Points(p1:pmodel.Point, p2:pmodel.Point, p3:pmodel.Point):
    #TODO generate circle model
    circ=CircleModel(0,0,1)
    return circ
