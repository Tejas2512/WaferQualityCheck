import pandas as pd
import json
import os
from mongoops import MongoOps


# Define file paths
schema_file = "schema_training.json"
data_dir = "Training_Batch_Files"
db = MongoOps()

# Load schema checks from JSON
with open(schema_file) as file:
    checks = json.load(file)

# Function to check the file name format
def name_check(name):
    parts = name.split('_')
    return (len(parts) == 3 and
            len(parts[1]) == checks['LengthOfDateStampInFile'] and
            len(parts[2].split('.')[0]) == checks['LengthOfTimeStampInFile'])

# Process each file in the data directory
for filename in os.listdir(data_dir):
    if name_check(filename):
        data = pd.read_csv(os.path.join(data_dir, filename))
        if len(data.columns) == checks['NumberofColumns']:
            data.columns = list(checks['ColName'].keys())
            try:
                data = data.astype(checks['ColName'])
                documents = data.to_dict(orient="records")
                db.add(documents)
            except ValueError as e:
                print(f"Data type conversion error in {filename}: {e}")
        else:
            print(f"Column count mismatch in {filename}")
    else:
        print(f"Invalid file name format in {filename}")
