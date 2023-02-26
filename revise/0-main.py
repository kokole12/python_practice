#!/usr/bin/python3
Comedian = __import__('0-revise').Comedian

if __name__ == "__main__":

    comedian = Comedian("James", "Alison", 8)
    # print(comedian.__str__())
    # print(comedian.__repr__())
    print(comedian)