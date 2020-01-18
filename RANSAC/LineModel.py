import Point as pt
import math


class LineModel:
    """Describes the equation of a straight line in ax+by+c format"""
    SMALL=0.001
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

    def get_slope(self):
        if (math.fabs( self.B ) < 0.001):
            raise Exception("Infinit slope")
        else:
            slope=-self.A/self.B
            return slope
    #
    #Returns inclination of the line with positive X axis
    #
    def get_inclination(self):
        if (math.fabs( self.B ) < 0.001):
            return math.pi/2;
        else:
            slope=-self.A/self.B
            angle=math.atan(slope)
            return angle
    #
    #Gets the Y intercept of the line, if infinite then math.inf
    #
    def yintercept(self):
        intercept=math.inf
        if (math.fabs(self.B) > LineModel.SMALL):
            intercept=-self.C/self.B;
        return intercept
    #
    #Gets the X intercept of the line, if infinite then math.inf
    #
    def xintercept(self):
        intercept=math.inf
        if (math.fabs(self.A) > LineModel.SMALL):
            intercept=-self.C/self.A
        return intercept

    #
    #Create a friendly display which shows all attributes of the Line
    #
    def display_polar(self):
        origin=pt.Point(0,0)
        distance_origin=self.compute_distance(origin)
        deg_per_radian=90*2/math.pi;
        angle=self.get_inclination() * deg_per_radian; 

        #   slope= -a/b
        #   yint= -c/b
        #   xint= -c/a
        y_intercept=self.yintercept()
        x_intercept=self.xintercept()

        display=("POLAR radius=%f  angle=%f     y_int=%s    x_int=%s" % (distance_origin,angle,y_intercept,x_intercept))
        return display
