# Function to add elements to a list
def add_students(student_list):
    n = int(input("How many students? "))
    for i in range(n):
        name = input("Enter student name: ")
        student_list.append(name)

# Function to display list elements
def display_students(student_list):
    print("\nStudent List:")
    for student in student_list:
        print(student)

# Function to search an element in list
def search_student(student_list, name):
    if name in student_list:
        print(name, "found in the list")
    else:
        print(name, "not found")

# Main program
students = []

add_students(students)
display_students(students)

search_name = input("\nEnter name to search: ")
search_student(students, search_name)
