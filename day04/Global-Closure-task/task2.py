def make_greeting(language):
    
    def greet(name):
        if language == "english":
            print("Hello,",name)
        elif language == "hindi":
            print("Namaste,",name) 
            
    return greet
    
g1=make_greeting("english")
g2=make_greeting("hindi")

g1("Riya")
g2("Aman")               