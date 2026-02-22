a=12
b=20
c=82
print("The numbers are",a,b,c)
print("Using WHILE loop:")
i=1
while i<=5:
    if i==3:
        i+=1
        continue          # skip 3
    print(i)
    i+=1