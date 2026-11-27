def fun(lst,index):
 try: 
    
    print(lst[index])
  
        
 except IndexError:
   return None

lst=[0,1,2,3,4]

print(fun(lst,2))
print(fun(lst,8))