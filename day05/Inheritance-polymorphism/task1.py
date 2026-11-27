class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Student(Person):
    def __init__(self,course,name,age):
        super().__init__(name,age)
        
        self.course=course
        
    def study(self):
        print(f"{self.name} is studying {self.course} at age {self.age}")
        
s1=Student("Python","Aaliya",18)

s1.study()


      