# Function with no arguments and no return value
def greet():
    print("Welcome to Python")
    
def add(a, b):
    print("Sum:", a + b)

def multiply(a, b):
    return a * b

def power(base, exp=2):
    return base ** exp

greet()
add(10, 20)

result = multiply(5, 4)
print("Multiplication:", result)

print("Power:", power(3))
print("Power:", power(2, 3))
