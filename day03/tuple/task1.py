def calculate_marks(marks):
    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)

    return (lowest, highest, average)

student_marks = [78, 85, 92, 67, 88]
result = calculate_marks(student_marks)

lowest_mark, highest_mark, average_mark = result
print("Lowest Mark:", lowest_mark)
print("Highest Mark:", highest_mark)
print("Average Mark:", average_mark)