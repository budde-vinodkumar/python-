arr = [1, 2, 4, 5]
n = 5

for i in range(1, n + 1):
    if i not in arr:
        print("Missing number:", i)
        break
