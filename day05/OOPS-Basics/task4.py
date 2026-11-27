class Employee:
    def __init__(self,salary):
        self.__salary=salary
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        if salary > self.__salary:
           self.__salary=salary
           print("Salary increased successfully")
        else:
            print("salary cannot be decreased")        
            
e1=Employee(20000)

print("Current salary:",e1.get_salary())

e1.set_salary(25000)
print("New Salary:",e1.get_salary())

e1.set_salary(18000)
print("Salary:",e1.get_salary())

            