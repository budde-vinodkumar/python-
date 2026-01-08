age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")


#Check if a number is even or odd
number = 7
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#Find the largest of three numbers
num1 = 10
num2 = 25
num3 = 15
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2      

else:
    largest = num3
print("The largest number is:", largest)


#break statement in a loop
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#continue statement in a loop
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#pass statement
for i in range(3):
    if i == 1:
        pass
    print(i)

#one more example of if-else
for i in range(1, 8):

    if i == 2:
        continue          # skips number 2

    elif i == 5:
        pass              # does nothing, just a placeholder

    elif i == 7:
        break             # stops the loop completely

    else:
        print(i)
