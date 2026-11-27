class InvalidAge(Exception): 
    pass
    
def register_user(age):
    
        if age < 0 or age >120:
          raise InvalidAge(age)
     
        print("User register succesfully")     
    
try:   
   register_user(20)
   register_user(121) 
  
except InvalidAge as error: 
     print("Invali age:",error)