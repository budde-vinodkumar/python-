
numbers = [10, 20, 30, 40]
print(numbers[0])          # first element
print(numbers[-1])         # last element

numbers.append(50)

numbers.extend([60, 70])
numbers.insert(1, 15)
numbers[2] = 25
numbers.remove(40)
numbers.pop()
numbers.pop(0)
temp_list = numbers.copy()
temp_list.clear()

print(numbers.index(30))
print(numbers.count(20))
print(numbers.count(100))

numbers.append(30)
print(numbers.count(30))
numbers.sort()
numbers.reverse()
new_list = numbers.copy()

print(len(numbers))

print(25 in numbers)
print(100 not in numbers)

for n in numbers:
    print(n)

print("Final List:", numbers)
print("Copied List:", new_list)
