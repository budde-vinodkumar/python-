balance = 10000
pin = 1234

entered_pin = int(input("Enter your PIN: "))

if entered_pin != pin:
    print("Wrong PIN. Access Denied.")
else:
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Amount deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance and amount > 0:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid option. Try again.")
