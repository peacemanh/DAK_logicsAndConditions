import json

# File paths (adjust them to your actual file locations)
input_file = 'conditionSetsConfig.json'  # The file containing the original JSON data
output_file = 'updated_data.json'  # The file to write the updated JSON data to

# Read the JSON data from the input file
with open(input_file, 'r') as file:
    data = json.load(file)

# Remove 'logic_key' from each dictionary in the list
for item in data:
    if 'logic_key' in item:
        del item['logic_key']

# Write the updated JSON data to the output file
with open(output_file, 'w') as file:
    json.dump(data, file, indent=2)

print("logic_key has been removed and JSON has been written to the output file successfully.")
