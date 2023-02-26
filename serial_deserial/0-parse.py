#!/usr/bin/python3
import json
from pprint import pprint

data = '''
{
    "name": "Json",
    "location": "Koboko",
    "subsidiaries": [
        {
            "country": "Uganda"
        },
        {
            "country": "South sudan"
        }
    ]
}
'''

if __name__ == "__main__":
    pydict = json.loads(data)
    print(type(pydict))
    pprint(pydict)