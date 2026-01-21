# Tuple of students, each student has (roll_no, details_dict)
students = (
    (101, {"name": "Amit", "marks": 85, "grade": "A"}),
    (102, {"name": "Neha", "marks": 90, "grade": "A+"}),
    (103, {"name": "Rahul", "marks": 72, "grade": "B"})
)

# Display all student details
for roll, details in students:
    print("Roll No:", roll)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("Grade:", details["grade"])
    print("--------------------")

# Access specific student data
print("Second student name:", students[1][1]["name"])
