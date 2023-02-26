#!/usr/bin/python3
'''printing characters in string'''

name = input("Enter your name: ")

for n in range(5):
    print(n)
for c in name:
    if c == "k":
        pass
    else:
        print(c * 3)
    
else:
    print("characters printed")