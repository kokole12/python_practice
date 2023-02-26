#!/usr/bin/python3
import json

json_file = "amzon.json"

if __name__ == "__main__":
    try:
        with open(json_file, 'r') as f:
            jdata = json.load(f)
        print(type(jdata))
        print(jdata)
    except Exception as e:
        print(e)

