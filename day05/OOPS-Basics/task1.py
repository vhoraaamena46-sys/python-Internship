class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year= year
        
    def display_info(self):
        print(f"My car is {self.brand}{self.model}, year{self.year}.")
        
c1=Car("Toyota", "Fortuner", 2024)
c2=Car("Honda","City", 2023)
c3=Car("Tata","Nexon", 2023)

c1.display_info()
c2.display_info()
c3.display_info()
              