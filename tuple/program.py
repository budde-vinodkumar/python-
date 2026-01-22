n = int(input("Enter n: "))
lst = []

for i in range(n):
    lst.append(input("Enter value: "))

t = tuple(lst)
print(t)
