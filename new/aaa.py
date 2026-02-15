arr = [2, 2, 1, 2, 3, 2, 2]
n = len(arr)

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    if value > n // 2:
        print("Majority element:", key)
        break
