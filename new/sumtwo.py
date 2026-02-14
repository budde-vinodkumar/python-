arr = [2, 7, 11, 15]
target = 9

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            found = True
            break
    if found:
        break
