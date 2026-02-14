arr = [1, 2, 3, 4, 5]
k = 2

k = k % len(arr)   # handle large k
rotated = arr[-k:] + arr[:-k]

print("Rotated array:", rotated)
