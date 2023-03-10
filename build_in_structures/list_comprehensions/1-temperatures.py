#!/usr/bin/python3
temps = [("Berlin", 29), ("cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26)]
c_to_f = lambda data: (data[0], 9/5 * data[1] + 32)
print(list(map(c_to_f, temps)))
