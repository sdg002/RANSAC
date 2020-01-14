import Point as pt
class LineModel:
    """Describes the equation of a straight line in ax+by+c format"""
    def __init__ (self, a:float,b:float,c:float):
        self.A=a
        self.B=b
        self.C=c
        pass
    A=0
    B=0
    C=0

    #
    #Compute distance of the point from the model line
    #
    def get_distance(self,point:pt.Point):
        return 1.1 #TO BE DONE

