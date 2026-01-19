# Creating a tuple
t = (10, 20, 30, 20)

print(t[0])        
print(t[-1])    

print("Length:", len(t))

print("Count of 20:", t.count(20))

print("Index of 30:", t.index(30))

print("Slice:", t[1:3])

print(20 in t)
print(50 not in t)

for item in t:
    print(item)

mixed = (1, "Python", 3.5, True)
print(mixed)

a, b, c, d = mixed
print(a, b, c, d)
