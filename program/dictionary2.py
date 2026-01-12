# Employee Dictionary Program

employee = {
    "id": 201,
    "name": "Ravi",
    "department": "IT",
    "salary": 30000
}

print("Employee Details:")
for key, value in employee.items():
    print(key, ":", value  )
employee["salary"] = 35000
employee["experience"] = 2   # years


if "department" in employee:
    print("\nDepartment exists")

employee.pop("department")
print("\nUpdated Employee Details:")
for key, value in employee.items():
    print(key, ":", value)
