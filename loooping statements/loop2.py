# Program to demonstrate looping statements

print("Using FOR loop:")
for i in range(1, 6):
    if i == 3:
        continue          # skip 3
    print(i)

print("\nUsing WHILE loop:")
num = 1
while num <= 5:
    if num == 4:
        break             # stop loop at 4
    print(num)
    num += 1
print("Loop ended.")   

numbers = [10, 20, 30, 40]
print("\nUsing FOR loop to iterate over a list:")   
for n in numbers:
    print(n)    
print("Final List:", numbers)
print("Length of List:", len(numbers))