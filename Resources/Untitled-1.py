import json

# Open the original JSON file
with open('establishments.json', 'r') as file:
    data = json.load(file)

# Write out the data in the expected format
with open('converted_establishments.json', 'w') as file:
    for record in data:
        json.dump(record, file)
        file.write('\n')