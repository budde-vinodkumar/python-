s = input("Enter a string: ")
count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print("Vowel count:", count)

# Count vowels in a string  
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)
