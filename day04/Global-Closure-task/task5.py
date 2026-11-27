mode="Global"

def enclosing():
    mode="enclosing"
    
    def local():
        mode="local"
        
        print("Mode is:",mode)
    local()
    
    print("Mode is:",mode)
    
enclosing()    
print("Mode is:",mode)