num = int(input("Enter a number: "))

if num <= 3:
    print("Not a Composite Number")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Composite Number")
            break
    else:
        print("Not a Composite Number")
