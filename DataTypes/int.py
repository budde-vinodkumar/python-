a=1
b=2
c=a+b
print(c)
d=c*3   
print(d)        
e=d-4
print(e)


f=e/2
print(f)    
g=f**2
print(g)
h=g%5

print(h)

#strings 
a= "Hello"
b="World"
c=a+" "+b
print(c)

d=c*3
print(d)

#lists
items=["apple","banana","cherry"]

print(items)
items.append("date")
print(items)
print(items[1])
print(len(items))
print(items[-1])
print(items)
print(items[0:2])

print(items)
items.remove("banana")
print(items)

items.sort()
print(items)
items.reverse()

print(items)
print(items)

print(items)
items.insert(1,"blueberry")

print(items)


print(items)
items.pop()
print(items)


#booleans
is_active=True
is_admin=False
print(is_active)
print(is_admin)
print(not is_active)
print(is_active and is_admin)
print(is_active or is_admin)
print(items)
print(items)

#integers
num1=10
num2=3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)

print(num1%num2)
print(num1//num2)

#flaots
price=99.99
discount=20.5
final_price=price-discount
print(final_price)

#decimals
from decimal import Decimal
price1=Decimal('19.99')
price2=Decimal('5.55')
total_price=price1+price2
print(total_price)