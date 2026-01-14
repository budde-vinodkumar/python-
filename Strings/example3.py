# Email validation
def validate_email(email):
    if "@" in email and "." in email:
        at_pos = email.index("@")
        dot_pos = email.rindex(".")

        if at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
            return True
    return False


# Password validation
def validate_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


# Main program
email = input("Enter email: ")
password = input("Enter password: ")

if validate_email(email):
    print("Email is valid")
else:
    print("Email is invalid")

if validate_password(password):
    print("Password is strong")
else:
    print("Password is weak")
