#!/usr/bin/python3
import json

data = {"name": "Winnie", "age": 16, "subcidiaries": [
    {"nationality": "`ugandan"}, {"nationality": "South sudanese"}
    ]}

fileString = "win.json"
if __name__ == "__main__":
    with open(fileString, 'w') as f:
        jstring = json.dump(data, f, indent=4)
    print("success")