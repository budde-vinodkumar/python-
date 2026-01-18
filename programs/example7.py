# Data Type Conversion Program

# Taking input
a = input("Enter a number: ")

# Converting string to int
num_int = int(a)

# Converting int to float
num_float = float(num_int)

# Converting int to complex
num_complex = complex(num_int)

# Converting number to string
num_str = str(num_int)

# Converting list to tuple and set
lst = [1, 2, 3]
tup = tuple(lst)
st = set(lst)

print("Integer:", num_int)
print("Float:", num_float)
print("Complex:", num_complex)
print("String:", num_str)
print("List:", lst)
print("Tuple:", tup)
print("Set:", st)
