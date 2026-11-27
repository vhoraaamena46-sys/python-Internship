class Stack:
    
    def __init__(self):
        self.__items=[]
        
    def push(self,item):
        self.__items.append(item)    
        
    def pop(self):    
        if len(self.__items) < 0:
            print("No item Found")
        else:
            return self.__items.pop()    
        
    def __str__(self):
        return f"Stack:,{self.__items}"    
    
s1=Stack()    

s1.push(20)
s1.push(90)
s1.push(80)



print(s1)

print("Removed:",s1.pop())
print(s1)