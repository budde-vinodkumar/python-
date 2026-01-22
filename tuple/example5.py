n = int(input("Enter number of elements: "))

elements = []

for i in range(n):
    value = int(input(f"Enter element {i+1}: "))
    elements.append(value)

# Convert list to tuple
t = tuple(elements)

print("Tuple elements:", t)

                    