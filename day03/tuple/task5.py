web_id={1000, 1001, 1002, 1003, 1000, 1002,1004,1003,1005}

def unique_id(id):
    result=[]
    
    for num in id:
        if num not in result:
            result.append(num)
    return result

output=unique_id(web_id)

print("Website ID's:", web_id)
print()
print("Website Unique ID's:", output)
print("Number of visitors:", len(output))
print()

#using set to get unique values
unique_web_id=set(web_id)

print("Unique Web IDs (using set):", unique_web_id)
print("Number of visitors:", len(unique_web_id))