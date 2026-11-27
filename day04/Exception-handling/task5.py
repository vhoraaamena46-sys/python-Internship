while True:
 try:

     number=int(input("Enter a number(1-10):"))
     if number >= 1 and number <= 10:
       print("Valid Number:",number)
       break
     else:
        raise ValueError
      
 except ValueError:
        print("Invalid Entry")