#!/usr/bin/python3
'''printing 1 - 10'''
counter  = 1

while counter < 10:
    if counter == 4:
        counter = counter+1
        continue
    if counter == 5:
        print("Five")
    else:
        print(counter)
    counter = counter+1
    
else:
    print("loop ended")