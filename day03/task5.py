students = [("Aamena", 85), ("jiya", 95), ("ikra", 72)]

students.sort(key=lambda student: student[1], reverse=True)

print("Students sorted by marks:")
print(students)