import json


def read():
    json_data = {}
    # Open and load the JSON data from the file
    with open('data.json', 'r') as f:
        json_data = json.load(f)
    return json_data

print(type({}))