def require_positive(func):
        def wrapper(a,b):
            if a <=0 or b <=0:
                print("Error:Enter positive numbers")
            else:
                func(a,b)
        return wrapper 
    
@require_positive
def divide(a,b):
    print("Division:", a/b)               
    
divide(10,2)
divide(10,-2)