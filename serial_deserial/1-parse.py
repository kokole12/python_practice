#!/usr/bin/python3
import json

data = {"name": "Winnie", "age": 16, "subcidiaries": [
    {"nationality": "`ugandan"}, {"nationality": "South sudanese"}
    ]}


if __name__ == "__main__":
    jString = json.dumps(data, indent=4)
    print(jString)
