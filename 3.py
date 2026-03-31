import json
import os

DATA_FILE = 'data/students.json'

def ensure_file():
    if not os.path.exists(DATA_FILE):
        os.makedirs('data', exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def load_data():
    ensure_file()
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    ensure_file()
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)