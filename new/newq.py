arr = [2, 2, 1, 2, 3, 2, 2]
n = len(arr)

for i in arr:
    if arr.count(i) > n // 2:
        print("Majority element:", i)
        break
