# input function in python 

a = input() 
print(int(a)+int(a))
# input function always read input value as string

name = input("enter your name:")
print(f"welcome {name}to python tutorial series")

age = input("enter your age:")
print(f"ohh you're just {age}")
print(f"so next year you will be {int(age)+1}")

# multiple input for users 
x= input("enter first number ")
y= input("enter second number")
print(f"sum of {x} & {y} is {int(x)+int(y)}")

# HW:  write a program to input studant name and marks of 3 subject
#print name and persentage 
x= input("enter your name ")
y= input("marks of suject 1")
z= input("marks of subject 2")
r= input("marks of subject 3")
print(f"my name is {x} & i have scored persentage { ((int(y)+int(z)+int(r))/3)}")





print("thank you for using this program")