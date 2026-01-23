# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# User input
n = int(input("Enter a number: "))

# Function call
result = check_even_odd(n)
print("The number is:", result)
