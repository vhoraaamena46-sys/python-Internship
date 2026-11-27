import time

def timer(func):
    def wrapper():
        start=time.time()
        
        func()
        
        end=time.time()
        print("Time taken:", end - start,"second")
        
    return wrapper
    
@timer
def calculate_sum():
    total=0
    
    for i in range(1,1000001):
        total=total+i
        
    print("Sum:", total)
    
calculate_sum()