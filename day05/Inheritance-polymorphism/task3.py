class Account:
    def get_interset_rate(self):
      return 4  
class SavingAccount(Account):    
    def get_interset_rate(self):
          return 5

class FixedDeposit(Account):    
    def get_interset_rate(self):
          return 7
      
a1=Account()
a2=SavingAccount()
a3=FixedDeposit()  
    
lst=[a1,a2,a3]      
    
for i in lst:
      print("Interset rate:",i.get_interset_rate(), "%")