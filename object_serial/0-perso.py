#!/usr/bin/python3
import json


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Winnie", 18)
""" the first option to serialize the data"""
jsonfile = f'{{"name": {person.name}, "age": {person.age}}}'
print(jsonfile)

""" using the json encoder function"""
def encoder_person(person):
    if isinstance(person, Person):
        return{'name': person.name, 'age': person.age}
    raise TypeError(f'object {person} is not of type Person')

jsonString = json.dumps(person, default=encoder_person, indent=4)
print()
print(jsonString)

""" using the encoder class"""
class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Person):
            return {'name': o.name, 'age': o.age}
        return super().default(o)

jstring = json.dumps(person, cls=PersonEncoder, indent=4)
print()
print(jstring)


encoded_person = PersonEncoder().encode(person)
print()
print(encoded_person)
