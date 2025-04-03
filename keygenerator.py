import json

# Load the configuration from the specified JSON file

with open(r'C:\Users\hp\Desktop\DAK_logicsAndConditions\calculationsWithoutFormulaConfig.json', 'r') as file:
    config = json.load(file)

# Adjust the 'action_key' values sequentially, starting from 0
for idx, item in enumerate(config, start=0):
    item['logic_key'] = idx

# Write the updated configuration to a new file
with open('FP_CL.json', 'w') as file:
    json.dump(config, file, indent=4)

# This script creates a file 'FP_DS.json' by adjusting the 'action_key' sequentially.
# After generating the file, copy the updated content and paste it into the original file.

# If working with skip logic, rename the file and replace the term 'action_key' with 'logic_key'.
