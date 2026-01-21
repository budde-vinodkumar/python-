# Nested tuple for company departments and employees
company = (
    ("HR", ((101, "Amit"), (102, "Neha"))),
    ("IT", ((201, "Rahul"), (202, "Sneha"))),
    ("Sales", ((301, "Arjun"),))
)

# Display company details
for dept in company:
    dept_name, employees = dept
    print("\nDepartment:", dept_name)

    for emp in employees:
        emp_id, emp_name = emp
        print("Employee ID:", emp_id, "Name:", emp_name)

# Access specific data
print("\nFirst employee of IT:", company[1][1][0][1])
