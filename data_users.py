import json
import os


def load_data(data):
    if os.path.exists(data):
        try:
            with open(data, "r", encoding="UTF-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
    return data


def save_data(user_data, data):
    with open(data, "w", encoding="UTF-8") as f:
        json.dump(user_data, f)
