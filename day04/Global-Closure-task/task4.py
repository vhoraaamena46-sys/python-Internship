def outer():
    status="pending"
    
    def inner():
       nonlocal status
       status="Continue"
       
       
    inner()
    print("Current Status:",status)
outer()    
   