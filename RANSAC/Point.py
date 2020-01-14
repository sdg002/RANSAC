

class Point:
    """Represents a point in 2 dimensional space"""
    idcounter=0
    def __init__(self, x,y):
        self.X=x
        self.Y=y
        self.ID=Point.idcounter+1
        Point.idcounter+=1
    def __str__(self):
        s="x=%d y=%d" % (self.X,self.Y)
        return s
    ID=0
    X=0
    Y=0

