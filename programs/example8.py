# IMPLICIT TYPE CONVERSION
a = 10        # int
b = 2.5       # float

result = a + b    # int + float → float automatically
print("Implicit Conversion Result:", result)
print("Type:", type(result))


# EXPLICIT TYPE CONVERSION
x = "20"          # string
y = int(x)        # string → int (manual conversion)

z = y + 5
print("Explicit Conversion Result:", z)
print("Type:", type(z))
