srting=23344
file=open("file.txt","w")
file.write(str(srting)) 
file.close()
file=open("file.txt","r")
print(file.read())  
