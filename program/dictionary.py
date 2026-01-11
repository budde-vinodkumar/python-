# Student Dictionary 

student = {
    "roll_no": 101,
    "name": "Vinnu",
    "course": "Python",
    "marks": 85
}

print("Student Details:")
print("Roll No:", student["roll_no"])
print("Name:", student["name"])
print("Course:", student["course"])
print("Marks:", student["marks"])

student["marks"] = 90
student["grade"] = "A"
student.pop("course")
print("\nUpdated Student Details:")
for key, value in student.items():
    print(key, ":", value)
