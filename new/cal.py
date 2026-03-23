
def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b


# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 1: Addition
add_result = addition(num1, num2)
print("Addition result:", add_result)

# Step 2: Multiplication
mul_result = multiplication(num1, num2)
print("Multiplication result:", mul_result)