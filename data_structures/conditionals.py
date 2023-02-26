#!/usr/bin/python3
print("welcome to this awesome app")
user_name = "k12"
password = "123jj"
username = input("Enter your username: ")
passworde = input("Enter password" ).lower()

if user_name == username and password == passworde:
    print("you are successfully logged in")
elif user_name == username:
    print('wrong password')
else:
    print("invalid credentials")
 
