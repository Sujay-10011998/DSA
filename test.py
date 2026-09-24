import json
 
# Name of the txt file
txt_file = 'abc.txt'
 
# Name of the json file
json_file = 'abc.json'
 
# Read the lines from the txt file
with open(txt_file, 'r') as f:
    lines = f.read().splitlines()
 
# Write the lines to a json file
with open(json_file, 'w') as f:
    json.dump(lines, f)