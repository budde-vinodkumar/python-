# Function to check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Main program
num = int(input("Enter a number: "))
result = check_even_odd(num)
print("The number is:", result)
