# Program to demonstrate looping statements

print("Using FOR loop:")
for i in range(1, 6):
    if i == 3:
        continue          # skip 3
    print(i)


numbers = [10, 20, 30, 40]
print("\nUsing FOR loop to iterate over a list:")   
for n in numbers:
    print(n)    
print("Final List:", numbers)
print("Length of List:", len(numbers))