class Inventory:
    def __init__(self,items):
        self.__items=items
        
    def __len__(self):  
        return len(self.__items)
    
    def  __getItem__(self,index):
        return self.__items[index]
    
i1=Inventory(["laptop","Mouse","keyboard","Monitor"])

print("Total Items:",len(i1))    
print(i1[0])
print(i1[2])