class Bird:
    def fly(self):
        print("Birds are  flying")
    
class Airplane:
    def fly(self):
            print("An airplabe is flying")
        
class Drone:        
    def fly(self):
            print("Drone can also fly")

def flying(obj):
    obj.fly()            
        
c1=Bird()
c2=Airplane()   
c3=Drone()     

flying(c1)
flying(c2)
flying(c3)