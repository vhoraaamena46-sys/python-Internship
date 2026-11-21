numbers = [12, 45, 12, 67, 89, 45, 23, 67, 90, 12, 34, 56, 89, 23, 78]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List:", numbers)
print("List Without Duplicates:", unique_numbers)