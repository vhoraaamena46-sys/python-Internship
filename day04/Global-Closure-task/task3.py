def make_counter():
    count=0
    
    def counter():
        nonlocal count
        count=count+1
        return count
   
    return counter
    
    
c1=make_counter()
c2=make_counter()    

c1()
c1()
c1()

c2()
c2()

print("Counter 1:",c1())
print("Counter 2:",c2())