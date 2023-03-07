#!/usr/bin/python3
name = input("enter your name: ")
lastname = input("enter your lastname: ")
age = int(input("enter your age: "))

print("Your name is %s %s and your %d years" %(name, lastname, age))
# new style formatting
print("your name is {} {} and you are {} years old".format(name, lastname, age))
print()
print("your name is {:s} {:s} and you are {:d} years old".format(name, lastname, age))
# using the indices
print()
print("your name is {1} {0} and you are {2} years old".format(name, lastname, age))
