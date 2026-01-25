# Function definitions

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Menu-driven program
while True:
    print("\n--- MENU ---")
    print("1. Reverse Number")
    print("2. Sum of Digits")
    print("3. Even or Odd")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Program exited")
        break

    num = int(input("Enter a number: "))

    if choice == "1":
        print("Reversed Number:", reverse_number(num))

    elif choice == "2":
        print("Sum of Digits:", sum_of_digits(num))

    elif choice == "3":
        print("Number is:", even_odd(num))

    else:
        print("Invalid choice")
