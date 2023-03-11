#!/usr/bin/python3

common_element = __import__('3-common_element').common_element

if __name__ == '__main__':

    set_1 = {"python", "C", "Java"}
    set_2 = {"Bash", "C", "Ruby"}

    c_set = common_element(set_1, set_2)
    print(sorted(list(c_set)))
