def lst(mylist):
    
  return frozenset(mylist)

mylist=[1,2,3,4,5]
print("My list is:", mylist)

print("Frozen set is:", lst(mylist))