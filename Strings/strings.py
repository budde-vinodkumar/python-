a="vinnu"
b="manna"
c=a+b       
print(c)

d="vinnu "
e="manna"
f=d+e
print(f)
g="vinnu"

h="manna"
i=g+" "+h
print(i)

j="vinnu"
k="manna"
l=j+"-"+k
print(l)

m="vinnu"
n="manna"
o=m+", "+n
print(o)

p="vinnu"   
q="manna"
r=p+" & "+q
print(r)

#string concatenation with numbers
s="vinnu"
t=5
u=s+str(t)
print(u)
v="vinnu"
w=10
x=v+" "+str(w)
print(x)

    #string concatenation in a loop
for i in range(1, 6):
    str1="vinnu"
    str2="manna"
    result=str1+" "+str2+" "+str(i)
    print(result)

#string concatenation with special characters
str3="vinnu"
str4="manna"
result2=str3+"@"+str4
print(result2)
str5="vinnu"
str6="manna"
result3=str5+"#"+str6
print(result3)


#string concatenation with empty strings
str7="vinnu"
str8=""
result4=str7+str8+"manna"
print(result4)
str9=""
str10="manna"
result5=str9+"vinnu"+str10
print(result5)

#string concatenation with long strings
str11="vinnu "*5
str12="manna "*5
result6=str11+str12
print(result6)
#string concatenation with user input
user_str1=input("Enter first string: ")
user_str2=input("Enter second string: ")
result7=user_str1+" "+user_str2
print("Concatenated String:", result7)
#string concatenation with string methods
str13="vinnu"
str14="manna"
result8=str13.upper()+" "+str14.lower()
print(result8)
str15="vinnu"
str16="manna"

result9=str15.capitalize()+" "+str16.capitalize()
print(result9)      


    #string concatenation with formatting
name1="vinnu"
name2="manna"
age1=25
formatted_str1="{} is {} years old and {} is {} years old.".format(name1, age1, name2, age1+2)
print(formatted_str1)
formatted_str2=f"{name1} works with {name2}."
print(formatted_str2)
formatted_str3="{0} & {1} are colleagues.".format(name1, name2)
print(formatted_str3)
