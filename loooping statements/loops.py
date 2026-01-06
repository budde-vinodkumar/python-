#for loop
for i in range(1, 6):
    print(i)

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#nested loop
num = 7

for i in range(2, num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

#loop with else

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Completed")
    print("Loop Ended")

#loop with continue



for i in range(5):
    if i == 2:
        continue
    print(i)
print("Loop Finished")
#loop with pass
for i in range(5):
    if i == 3:
        pass
    print(i)
print("End of Loop")
#loop with break
for i in range(5):
    if i == 3:
        break
    print(i)

print("Loop Terminated Early")

#nested loops example
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")                    

