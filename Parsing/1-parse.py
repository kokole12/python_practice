#!/usr/bin/python3
import json
super_hero = {
    "justice_league": [
        "superman",
        "Batman",
        "Black Adam"
    ],
    "Avengers": [
        "Thor",
        "Iron man",
        "Hulk"
    ]
}

if __name__ == "__main__":
    jstring = json.dumps(super_hero, indent=4)
    print(type(jstring))
    print(jstring)
