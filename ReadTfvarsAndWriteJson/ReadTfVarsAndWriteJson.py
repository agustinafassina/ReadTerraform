import json

# Read the file .tfvars
with open('dev.tfvars', 'r') as file:
    tfvars_data = file.read()

# Convert to JSON format
tfvars_json = {}
for line in tfvars_data.split('\n'):
    if not line.strip() or line.startswith('#'):  # Ignore blank lines or comments
        continue
    key, value = line.split('=', 1)
    tfvars_json[key.strip()] = value.strip().replace('"', '')

# Save in a file .json
with open('dev.json', 'w') as file:
    json.dump(tfvars_json, file, indent=4)

print('File .tfvars converted to .json successfully.')