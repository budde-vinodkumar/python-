# Function to find sum of digits
def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# User input
n = int(input("Enter a number: "))

# Function call
result = sum_of_digits(n)
print("Sum of digits:", result)
