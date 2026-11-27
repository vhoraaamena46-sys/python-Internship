class wallet:
    def __init__(self,balance):
        self.__balance=balance
        
    def  deposit(self):
     amount=int(input("Enter amount to Deposit:"))  
     if amount < 0:
            print("Cannot deposit")
     else:
            self.__balance+=amount
            print("amount Deposited")  
            
    def withdraw(self):
     amount=int(input("Enter amount to Withdraw:"))
              
     if amount <= 0 or amount > self.__balance:
                print("Cannot Withdrw")
     else:
                self.__balance -=amount
                print("amount WithDraw")  
    
    @property            
    def balance(self):
       return self.__balance          
                  
w1=wallet(9000)
w1.deposit()
w1.withdraw()
print("Amount is:",w1.balance)                  
                  