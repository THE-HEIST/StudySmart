import json
import os

def load_database(db_path, db_type):
    f = open(db_path, db_type)
    return json.loads(f)