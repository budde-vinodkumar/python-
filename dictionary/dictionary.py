# Creating a dictionary
student = {
    "name": "Vinnu",
    "age": 22,
    "course": "Python"
}
print(student["name"])

print(student.get("age"))

print(student.keys())

print(student.values())

print(student.items())

student["age"] = 23

student.update({"city": "Hyderabad", "course": "AI"})

student.pop("city")

student.popitem()

student.setdefault("gender", "Male")

student_copy = student.copy()
student_copy.clear()
print(len(student))
print("name" in student)

keys = ["id", "email"]
new_dict = dict.fromkeys(keys, "Not Assigned")

print(student)
print(new_dict)
