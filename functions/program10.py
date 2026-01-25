# Function to display tuple elements
def display(t):
    print("Tuple elements:")
    for item in t:
        print(item)

def sum_tuple(t):
    total = 0
    for item in t:
        total += item
    return total
\
def search(t, value):
    if value in t:
        return "Element found"
    else:
        return "Element not found"

# Main program
numbers = (10, 20, 30, 40)

display(numbers)

print("Sum of tuple:", sum_tuple(numbers))

value = int(input("Enter element to search: "))
print(search(numbers, value))
