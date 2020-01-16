import Point as pt
import math
class LineModel:
    """Describes the equation of a straight line in ax+by+c format"""
    def __init__ (self, a:float,b:float,c:float):
        self.A=a
        self.B=b
        self.C=c
        pass
    def __str__(self):
        display= ("A=%f B=%f C=%f") % (self.A,self.B,self.C)
        return display

    #
    #Compute distance of the point from the model line
    #
    def compute_distance(self,point:pt.Point):
        numerator=self.A*point.X + self.B*point.Y + self.C
        denominator=math.sqrt(self.A*self.A + self.B*self.B)
        distance=math.fabs( numerator/denominator)
        return distance

