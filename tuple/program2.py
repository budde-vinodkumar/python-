# Taking user input
n = int(input("Enter number of elements: "))
data = []

for i in range(n):
    data.append(input("Enter value: "))

# Creating list and tuple
lst = data
tup = tuple(data)

print("\nList:", lst)
print("Tuple:", tup)

# Modifying list (allowed)
lst.append("NEW")
print("\nAfter modifying list:")
print("List:", lst)
