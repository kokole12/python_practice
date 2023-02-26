#!/usr/bin/python3
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
persn = Person("James", 23)
""" using the dictionary approach"""
jsonString = f'{{"name": {persn.name}, "age": {persn.age}}}'
print(jsonString)

def encode_person(persn):
        if isinstance(persn, Person):
            return {"name": persn.name, "age": persn.age}
        raise TypeError('object {} is not instance of person'.format(persn))

jstring = json.dumps(persn, default=encode_person, indent=4)
print(jstring)



class EncodePersn(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return  {"name": o.name, "age": o.age}
        return super().default(o)

jsonstring = json.dumps(persn, cls=EncodePersn, indent=4)
print(jsonstring)

    