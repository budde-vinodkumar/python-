queue = []

while True:
    print("\n--- QUEUE MENU ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = int(input("Enter element: "))
        queue.append(item)
        print("Element added")

    elif choice == "2":
        if queue:
            removed = queue.pop(0)
            print("Removed element:", removed)
        else:
            print("Queue is empty")

    elif choice == "3":
        print("Queue:", queue)

    elif choice == "4":
        print("Program exited")
        break

    else:
        print("Invalid choice")
