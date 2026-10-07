 # Data type in python 
a= 1
b = 1
print(a+b)
print(type(a)) # checking data type: integer

c = "1" 
d = "1"
print(c+d)
print(type(c)) # checking data type : string 

# basi data type in python
#1. Numerical
a1 = 1    #1.a  integer
a2 = 1.5  #1.b  float 
print(type(a2))
a3 = complex(3,5)  #1.c complex 
print(type(a3))
#2. sequance 
b1 = "ROHIT"  #2.a string 
b11 = '26'
print(type(b1))
b2 = [1,4,7,26,108,"ROHIT" ] #2.b list
print(type(b2))
b3 =(1,4,7,26,108,"ROHIT")  #2.c tuple 
print(type(b3)) 

#3. dictionary 
my_dictionary = {'name': 'Rohit','age': 19, 'city':'latur'}
print(type(my_dictionary))

#4. sets 
my_setes ={1,4,7,26,108,"ROHIT"}
print(type(my_setes))

#5.boolean 
bool1 = True
bool2 = False 
print(type(bool2))

#6. binary
# bytes, bytearray, meomaryview
byte1= b"Rohit" 
print(type(byte1))