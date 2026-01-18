# Taking input and converting to different data types

a = int(input("Enter an integer: "))
b = float(input("Enter a float number: "))
c = complex(input("Enter a complex number (e.g. 2+3j): "))
name = input("Enter a string: ")
flag = bool(input("Enter any value (True/False): "))

lst = list(input("Enter elements for list: ").split())
tup = tuple(lst)
st = set(lst)

dic = {"name": name, "number": a}

print(a, b, c, name, flag)
print(lst)
print(tup)
print(st)
print(dic)
