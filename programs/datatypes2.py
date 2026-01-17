a = 10                # int
b = 2.5               # float
c = 3 + 4j            # complex
name = "Python"       # string
flag = True           # boolean
lst = [1, 2, 3]       # list
tup = (4, 5)          # tuple
st = {6, 7}           # set
dic = {"id": 1}       # dictionary
x = None              # None type

print(a, b, c, name, flag, lst, tup, st, dic, x)
print(type(a))
print(type(b))  
print(type(c))
print(type(name))
print(type(flag))
print(type(lst))
print(type(tup))
print(type(st))
print(type(dic))
print(type(x))

# Demonstrating type conversion
a_float = float(a)        # int to float
b_int = int(b)          # float to int
c_str = str(c)          # complex to string
name_list = list(name)  # string to list
flag_int = int(flag)    # boolean to int
lst_tuple = tuple(lst)  # list to tuple
tup_set = set(tup)     # tuple to set
st_list = list(st)     # set to list
dic_str = str(dic)     # dictionary to string
x_str = str(x)         # None type to string
print(a_float)
print(b_int)
print(c_str)
print(name_list)
print(flag_int)
print(lst_tuple)
