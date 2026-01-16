n = int(input("Enter number of subjects: "))

total = 0

for i in range(1, n + 1):
    marks = int(input(f"Enter marks of subject {i}: "))
    total += marks

average = total / n
percentage = (total / (n * 100)) * 100

print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage)
