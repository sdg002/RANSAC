

class Point:
    """Represents a point in 2 dimensional space"""
    idcounter=0
    def __init__(self, x,y):
        self.X=x
        self.Y=y
        self.ID=Point.idcounter+1
        Point.idcounter+=1
    def __str__(self):
        s="ID=%d x=%d y=%d" % (self.ID,self.X,self.Y)
        return s

