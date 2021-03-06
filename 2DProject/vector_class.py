import math

class Vector:

    def __init__(self):
        self.x = 0
        self.y = 0
        
    def setVector(self,x,y):
        self.x = x
        self.y = y
    def getSize(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    def getVector(self):
        return self.x , self.y
    
    def Plus(self,x,y):
        self.x += x
        self.y += y

    def Minus(self,x,y):
        self.x -= x
        self.y -= y
    def normalizeVector(self):
        mag = math.sqrt(self.x*self.x + self.y*self.y)
        self.x /= mag
        self.y /= mag

    def dotVector(self,x,y):
        return self.x*x + self.y*y

    def angleBetweenVector(self,x,y):
        PI = 3.1415
        return(math.acos(self.dotVector(x,y) /
                         (self.getSize() * math.sqrt(x*x + y*y))) * (180/PI))

    def gravity(self):
        self.y -= 0.02

    def friction(self):
        if self.x >0:
            self.x -= 0.02
        elif self.x < 0:
            self.x += 0.02
