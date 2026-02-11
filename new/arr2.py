arr = [2, 5, 8, 12, 16, 23]
key = int(input("Enter number to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = True
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Element found")
else:
    print("Element not found")
