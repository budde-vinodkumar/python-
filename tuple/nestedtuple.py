# Nested tuple storing multiple student records
students = (
    (101, "Amit", 85),
    (102, "Neha", 90),
    (103, "Rahul", 78)
)

# Display all student records
print("Student Records:")
for student in students:
    roll, name, marks = student
    print("Roll:", roll, "Name:", name, "Marks:", marks)

# Access specific student
print("\nFirst student name:", students[0][1])
print("Second student marks:", students[1][2])
