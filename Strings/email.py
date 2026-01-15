# Function to validate email format
def validate_email(email):
    return "@" in email and "." in email


# Function to validate password strength
def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = has_lower = has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


# Function to check login using file
def login(email, password):
    try:
        file = open("users.txt", "r")
        for line in file:
            saved_email, saved_password = line.strip().split(",")
            if email == saved_email and password == saved_password:
                file.close()
                return True
        file.close()
    except FileNotFoundError:
        print("User file not found")
    return False


# Main program
email = input("Enter email: ")
password = input("Enter password: ")

if not validate_email(email):
    print("Invalid email format")
