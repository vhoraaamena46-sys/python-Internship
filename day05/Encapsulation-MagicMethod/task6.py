class Money:
    def __init__(self,money,currency):
        self.money=money
        self.currency=currency
        
        
    def __gt__(self,other):
        if self.currency != other.currency:
            raise ValueError("Differnt currency cannot be measured")
        else:
           return  self.money > other.money
        
    def __lt__(self,other):
       if self.currency != other.currency:
             raise ValueError("Differnt currency cannot be measured")
       else:
             return   self.money < other.money
                    
         
m1=Money(1000,"Pound")
m2=Money(3000,"Pound")



print(m1 > m2)
print(m1 < m2)

    
    
    

            
                               