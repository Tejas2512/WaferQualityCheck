import pandas as pd
import json
import os
from WaferQualityCheck.db.mongoops import MongoOps  # Assuming you have a separate module for MongoOps
import shutil


# Define file paths
SCHEMA_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__), "schema_training.json"))
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Training_Batch_Files"))
INVALID_FILES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "Invalid_Data"))


def load_schema_checks(schema_file):
    """Load schema checks from a JSON file and return them as a dictionary."""
    with open(schema_file) as file:
        return json.load(file)


def is_valid_filename(name, checks):
    """Check if a filename follows the expected format."""
    parts = name.split('_')
    return (
        len(parts) == 3
        and len(parts[1]) == checks['LengthOfDateStampInFile']
        and len(parts[2].split('.')[0]) == checks['LengthOfTimeStampInFile']
    )


def process_file(filename, checks, db):
    """Process a single file."""
    if is_valid_filename(filename, checks):
        data = pd.read_csv(os.path.join(DATA_DIR, filename))
        if len(data.columns) == checks['NumberofColumns']:
            data.columns = list(checks['ColName'].keys())
            try:
                data = data.astype(checks['ColName'])
                documents = data.to_dict(orient="records")
                db.add(documents)
            except ValueError as e:
                print(f"Data type conversion error in {filename}: {e}")
                shutil.move(src=os.path.join(DATA_DIR, filename), dst=INVALID_FILES_DIR)
        else:
            print(f"Column count mismatch in {filename}")
            shutil.move(src=os.path.join(DATA_DIR, filename), dst=INVALID_FILES_DIR)
    else:
        print(f"Invalid file name format in {filename}")
        shutil.move(src=os.path.join(DATA_DIR, filename), dst=INVALID_FILES_DIR)


def main(credentials="default"):
    """
        Main function to process files.
        :param credentials: The name of the credentials to use from the 'cred.json' file.
    """
    checks = load_schema_checks(SCHEMA_FILE)
    db = MongoOps(credentials=credentials)

    for filename in os.listdir(DATA_DIR):
        process_file(filename, checks, db)


if __name__ == "__main__":
    main()
