arr = [10, 20, 30, 40]
key = int(input("Enter number to search: "))

found = False
for i in arr:
    if i == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
