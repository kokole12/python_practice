#!/usr/bin/python3
import json
from pprint import pprint
data = '''
{
    "company": "Audible",
    "country": "USA",
    "subsidiaries": [
        {
            "company": "Auditble"
        },
        {
            "company": "Amazon go"
        }
    ]
}
'''

if __name__ == "__main__":
    jdata = json.loads(data)
    print(type(jdata))
    pprint(jdata)
    print(jdata['country'])
