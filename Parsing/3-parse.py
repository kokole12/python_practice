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

json_file_name = 'super_hero.json'
if __name__ == "__main__":
    with open(json_file_name, 'w') as f:
        json.dump(super_hero, f, indent=4)

