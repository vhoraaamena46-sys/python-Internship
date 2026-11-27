def make_validators(min_value):
    
    def check(num):
        if num >=min_value:
            print(num,"is valid")
        else:
            print(num,"is not valid ")
    return check       

v1=make_validators(10)
v2=make_validators(20)     
        
v1(15)
v2(5) 

v1(60)
v2(30)       