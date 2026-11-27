def safe_division(a,b):
 try:
     
    result=a/b
    
    print("Result:",result)
 except ZeroDivisionError as error:
     print("Cannot be Divide by Zero,",error)
 except TypeError as error:
     print("Invalid type,",error)       
  
 finally:
     print("Program Completed") 
     print()
     
safe_division(10,0)  
safe_division(20,10)
safe_division(10,"Two")