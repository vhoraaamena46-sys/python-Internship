order={
    "item":"laptop",
    "price":20000
 }
def process_order(order):
    try:
       item=order["item"]
       price=order["price"]
    except KeyError:
        print("Error: Missing key in order")    
       
    else:
        print("Item:",item)
        print("Price:",price)
        
    finally:
        print("Program completed") 

process_order(order)        
             