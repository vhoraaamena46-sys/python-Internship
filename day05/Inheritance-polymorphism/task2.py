class Employee:
    
    def __init__(self,sal):
        self.sal=sal
           
    
    def calculate_salary(self):
        return self.sal   
     
class Developer(Employee):
     def calculate_salary(self):
         bonus=5000   
         salary=super().calculate_salary()+bonus
         print("Salary after developer bonus:",self.sal) 
    
class Designer(Employee):
     def calculate_salary(self):
         bonus=4000   
         salary=super().calculate_salary()+bonus
         print("Salary after designer bonus:",self.sal)

c1=Developer(90000)  
c2=Designer(50000) 
      
c1.calculate_salary()
c2.calculate_salary()