num = int(input("Enter a number: "))

if num <= 1:
    print("Neither Prime nor Composite")

else:
    factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1

    if factors == 2:
        print("Prime Number")
    else:
        print("Composite Number")
