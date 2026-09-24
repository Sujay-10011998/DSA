#implicit -  Python interpreter automatically converts one data type to another without any user involvement
x = 10
print("type of x: ",type(x))
y = 10.6
print("type of y: ",type(y))
z = x + y
print(z)
print("type of z: ",type(z))

#explicit -  the data type is manually changed by the user as per their requirement
s = "10010"
c = int(s,2)
print ("After converting to binary : ", end="")
print (c)
e = float(s)
print ("After converting to float : ", end="")
print (e)
