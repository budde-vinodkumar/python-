# Dictionary to store student data
students = {}

# Function to add student
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    students[roll] = name
    print("Student added successfully")

# Function to view all students
def view_students():
    if not students:
        print("No students found")
    else:
        for roll, name in students.items():
            print("Roll:", roll, "Name:", name)

# Function to search student
def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        print("Student Name:", students[roll])
    else:
        print("Student not found")

# Function to delete student
def delete_student():
    roll = input("Enter roll number to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully")
    else:
        print("Student not found")

# Main menu
while True:
    print("\n--- STUDENT MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program exited")
        break
    else:
        print("Invalid choice")
