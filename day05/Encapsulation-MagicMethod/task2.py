class Fraction:
    def __init__(self,num,demo):
        self.num=num
        self.demo=demo
        
    def __add__(self,other):
        n=self.num *other.demo + other.num*self.demo    
        d=self.demo * other.demo
        
        return Fraction(n,d)
        
    def __str__(self):
        return f"{self.num}/{self.demo}" 
    

    
f1=Fraction(1,2)    
f2=Fraction(1,3)

f3=f1+f2

print(f3)