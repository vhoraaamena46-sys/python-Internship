class Vehicle:
    def material(self,mat):
     self.mat=mat
    
    
class car(Vehicle):
    def type(self,type):
        self.type=type
    
class SportCar(car):        
    def color(self,col):
       self.col=col
     
    def display(self):  
        print(f"materila is {self.mat} type is {self.type},color is {self.col}")   

c1=SportCar()

c1.material("Still")
c1.type("Gas") 
c1.color("Black")   
c1.display()   