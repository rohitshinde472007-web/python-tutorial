# casting in variables

a=1
print(type(a))

b = "1"
print(type(b))

c = int(b)
print(type(c))

print(a+int(b))

# all str type can't be casted into numerical type 
name ="Rohit"               
newname = int(name)

mynum = 26 
mynum2 = str(mynum)
print(type(mynum2))
 
f1 = 22.56
f2 = int(f1)
print(f2)
print(type(f2))

in1 = 26 
print(type(float(in1)))

# implicit type casting 
var1 = 10  # int type
var2 = 15.5 # float type
var3 = var1+var2
print(var3)

#explicit type   Cast
int_num =101
str_num = str(int_num)
print(type(str_num))