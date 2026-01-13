# Function to add student to file
def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    file = open("students.txt", "a")
    file.write(roll + "," + name + "," + marks + "\n")
    file.close()

    print("Student record added")


# Function to view all students
def view_students():
    try:
        file = open("students.txt", "r")
        print("\n--- Student Records ---")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print("Roll:", roll, "Name:", name, "Marks:", marks)
        file.close()
    except FileNotFoundError:
        print("No records found")


# Function to search student by roll number
def search_student():
    roll_search = input("Enter roll number to search: ")
    found = False

    try:
        file = open("students.txt", "r")
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print("Student Found →", name, marks)
                found = True
                break
        file.close()

        if not found:
            print("Student not found")

    except FileNotFoundError:
        print("File not found")


# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
