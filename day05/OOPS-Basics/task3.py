import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    @property
    def area(self):
        return math.pi*self.radius*self.radius
    
    @property
    def circumferenced(self):
        return 2 * math.pi * self.radius
    
c1=Circle(5)

print("Radius:",c1.radius)
print("Area:",c1.area)
print("Circumfferen:",c1.circumferenced)     
        