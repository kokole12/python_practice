#!/usr/bin/python3
import json
from pprint import pprint

jsonfile = "data.json"

if __name__ == "__main__":
    with open(jsonfile, 'r') as f:
        jdata = json.load(f)
    
    pprint(jdata)
    print(jdata['location'])

