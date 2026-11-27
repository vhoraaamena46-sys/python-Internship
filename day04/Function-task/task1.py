def build_invoice(name,*prices,**details):
    print("Customer Name:",name)
    
    total=sum(prices)
    print("Total Amount:",total)
    
    print("Extra Details:")
    for key,value in details.items():
        print(key,":",value)
        
build_invoice("Riya",100,200,30,
discount=50, tax=20)