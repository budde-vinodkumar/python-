# Tuple  (real-world example)
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print("Days of the Week:")
for day in days:
    print(day)

print("\nFirst day:", days[0])
print("Last day:", days[-1])

if "Sunday" in days:
    print("\nSunday is a holiday")
