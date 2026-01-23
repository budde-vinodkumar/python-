# Function to reverse a number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

# User input
n = int(input("Enter a number: "))

# Function call
result = reverse_number(n)
print("Reversed number:", result)
