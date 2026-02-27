vinnu=[1,2,3,4,5]
print(vinnu[0])          # first element
print(vinnu[-1])         # last element
vinnu.append(6)
vinnu.extend([7, 8])
vinnu.insert(1, 1.5)
vinnu[2] = 2.5
vinnu.remove(4)
vinnu.pop()
vinnu.pop(0)
temp_list = vinnu.copy()
temp_list.clear()
print(vinnu.index(3))
print(vinnu.count(2))
print(vinnu.count(10))
vinnu.append(3)
print(vinnu.count(3))
vinnu.sort()
vinnu.reverse()
new_list = vinnu.copy()
print(len(vinnu))
