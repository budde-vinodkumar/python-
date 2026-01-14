# Creating a string
text = "  Python Programming  "


print(len(text))

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

print(text.strip())     # both sides
print(text.lstrip())    # left side
print(text.rstrip())    # right side

print(text.replace("Python", "Java"))


print(text.find("Pro"))     # returns index
print(text.find("C++"))     # returns -1

print(text.count("m"))

print(text.isalpha())       
print("123".isdigit())      
print("abc123".isalnum())   

words = text.split()
print(words)

joined = "-".join(words)
print(joined)

sample = "Python"
print(sample[0])        
print(sample[-1])       
print(sample[1:4])      
print(sample[:3])       
print(sample[3:])       

print("Python" in text)
print("Java" not in text)

for char in sample: 
    print(char) 