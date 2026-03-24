lst=[1,2,2,3]
freq={}
for i in lst:
    freq[i]=freq.get(i,0)+1
print(freq)
print("Frequency of 2:", freq.get(2,0))