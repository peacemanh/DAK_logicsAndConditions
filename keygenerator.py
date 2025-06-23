import json

# Load the configuration from the specified JSON file
with open(r'/home/selamsew/GondarCares/DAK/logicsAndConditions/DAK_logicsAndConditions/samriCoSet.json', 'r') as file:
    config = json.load(file)

# Adjust the 'logic_key' values sequentially, starting from 0
for idx, item in enumerate(config, start=0):  # make sure config is a list
    item['action_key'] = idx

# Write the updated configuration to a new file
with open('samriCoSetUpdated.json', 'w') as file:
    json.dump(config, file, indent=4)

# This script creates a file 'FP_CL.json' by adjusting the 'logic_key' sequentially.
# After generating the file, you may copy the updated content into the original configuration file if needed.
