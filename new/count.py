
arr = [2, 2, 1, 2, 3, 2, 2]

candidate = None
count = 0

for num in arr:
    if count == 0:
        candidate = num
        count = 1
    elif num == candidate:
        count += 1
    else:
        count -= 1

print("Majority element:", candidate)
