#!/usr/bin/python3

only_different_elements = \
    __import__('4-only_different_elements').only_different_elements

if __name__ == "__main__":

    set_1 = {"python", "C", "Javascript"}
    set_2 = {"Bash", "C", "Ruby", "perl"}

    od_set = only_different_elements(set_1, set_2)

    print(sorted(list(od_set)))
